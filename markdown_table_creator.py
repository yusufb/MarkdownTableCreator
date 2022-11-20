import sublime_plugin, sublime

class MarkdownTableCreatorCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		
		self.settings = sublime.load_settings('markdown_table_creator.sublime-settings')

		DEBUG = self.settings.get('debug_mode', False)
		
		view = self.view
		
		for sel in view.sel():

			if DEBUG:
				import traceback
				try:
					new_content = self.create_table(view.substr(sel))
				except Exception as e:
					new_content = view.substr(sel) + "\n\n" + traceback.format_exc()
			else:
				new_content = self.create_table(view.substr(sel))

			view.replace(edit, sel, new_content)


	def create_table(self, content):
		
		if not content:
			return ''

		content = content.strip()

		if len(content) < 0:
			return ''

		lines = content.splitlines()

		new_content = []
		head_already_exists = False
		
		header_separators = self.settings.get('extra_header_separators', '')
		content_separators = self.settings.get('extra_content_separators', '')
		default_alignment = self.get_default_alignment()

		for index, line in enumerate(lines):

			line = line.strip(' |')

			if index == 0:
				new_content.append([])
				new_content.append([])

				for dx in header_separators:
					line = line.replace(dx, '|')

				data = line.split('|')

				widths = [0] * len(data)
				alignments = [0] * len(data)

				for i, d in enumerate(data):
					d = d.strip()

					if d.startswith(':') and d.endswith(':'):
						alignments[i] = 'c'
						if not self.is_line_header(lines[1] if len(lines)>1 else None): d = d[1:-1] 
					elif d.startswith(':'):
						alignments[i] = 'l'
						if not self.is_line_header(lines[1] if len(lines)>1 else None): d = d[1:] 
					elif d.endswith(':'):
						alignments[i] = 'r'
						if not self.is_line_header(lines[1] if len(lines)>1 else None): d = d[:-1] 
					else:
						alignments[i] = default_alignment

					widths[i] = max(widths[i], len(d))

					new_content[index].append(d)
					new_content[index+1].append('-')

			elif index == 1 and self.is_line_header(line):
				head_already_exists = True

				line = line.strip(' |')
				data = line.split('|')
				for i, d in enumerate(data):
					d = d.strip()
					if d.startswith(':') and d.endswith(':'):
						alignments[i] = 'c'
					elif d.startswith(':'):
						alignments[i] = 'l'
					elif d.endswith(':'):
						alignments[i] = 'r'
					else:
						alignments[i] = default_alignment #do we really want to use the default alignment?	

				continue		 

			else:

				new_content.append([])

				for dx in content_separators:
					line = line.replace(dx, '|')

				data = line.split('|')
				for i, d in enumerate(data):
					d = d.strip()

					widths[i] = max(widths[i], len(d))

					new_content[index if head_already_exists else index+1].append(d)

		params = {'widths': widths, 'alignments': alignments}
		
		return self.content_to_str(new_content, params)


	def is_line_header(self, line_content):
		if not line_content: return False

		return all(c in '- |:' for c in line_content)


	def content_to_str(self, content, params):

		c = ''
		widths = params['widths']
		alignments = params['alignments']

		for l, line in enumerate(content):

			if l == 1:
				c += '|'
				for i, d in enumerate(line):
					a = alignments[i]
					c += ' ' 

					if a == 'c':
						c += ':'

					c += '-'*widths[i]

					if a in ('c', 'r'):
						c += ':'

					c += ' |'

			else:
				c += '|' 

				for i in range(len(widths)):
					w = line[i] if i < len(line) else ' '
					c += ' ' + self.get_aligned_content(w, widths[i], alignments[i]) + ' |' 

			c += "\n"

		return c

	def get_space(self, alignment):
		if alignment == 'c':
			return 2

		if alignment == 'l':
			return 0

		if alignment == 'r':
			return 1

		
	def get_aligned_content(self, w, width, alignment):
		width +=  self.get_space(alignment)
		if alignment == 'c':
			return w.center(width)

		if alignment == 'l':
			return w.ljust(width)

		if alignment == 'r':
			return w.rjust(width)


	def get_default_alignment(self):
		try:
			da = self.settings.get('default_alignment', '').lower().strip()
			if da == 'center': return 'c'
			if da == 'right': return 'r'
			return 'l'
		except:
			return 'l'


