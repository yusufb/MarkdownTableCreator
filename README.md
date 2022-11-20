# Markdown Table Creator

**Markdown Table Creator** is a Sublime Text plugin that helps you create and reformat Markdown tables quickly.



https://user-images.githubusercontent.com/1588495/202923784-16f5d2a0-920d-4dbc-a58a-0a2861f8eceb.mov



#### Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Configuration](#configuration)

<a id="installation" name="installation"></a>
## Installation

### via Package Control

_TBA_

### Manual Installation

1. Open Sublime Text package directory with `Sublime Text > Preferences > Browse Packages...`.
2. Copy the files to `User` directory.


<a id="usage" name="usage"></a>
## Usage

### Create Markdown table

- Type 1+ header names, separated with `|` (or configured `extra_header_separators`)
- Type content data, separated with `|` (or configured `extra_content_separators`) _(optional)_
- Select the text you want to convert to Markdown table
- Select `Markdown Table Creator` from Command Palette, or hit `alt+shift+t`


### Reformat Markdown table

- Make any change in header/content data, alignment, or table structure 
- Select the Markdown table
- Select `Markdown Table Creator` from Command Palette, or hit `alt+shift+t`

<a id="examples" name="examples"></a>
## Examples

#### ▶ Only header information

**Before**

`City|Country|Population`

**After**

| City | Country | Population |
| ---- | ------- | ---------- |

---

#### ▶ If you defined `\` as separator in `extra_header_separators` such as `"extra_header_separators": "\\"`

**Before**

`City\Country\Population`

**After**

| City | Country | Population |
| ---- | ------- | ---------- |

---

#### ▶ You can also enter the data alongside the header

**Before**

```
City\Country\Population
London|UK|8M
Istanbul|Turkey|12M
```

**After**

| City     | Country | Population |
| -------- | ------- | ---------- |
| London   | UK      | 8M         |
| Istanbul | Turkey  | 12M        |

---

#### ▶ You can define the column alignment by putting `:` to the header

**Before**

```
City (Default Left)|:Country (Centered):|Population (Right):
London|UK|8M
Istanbul|Turkey|12M
```

**After**

| City (Default Left) |  Country (Centered)  |  Population (Right) |
| ------------------- | :------------------: | ------------------: |
| London              |          UK          |                  8M |
| Istanbul            |        Turkey        |                 12M |



<a id="configuration" name="configuration"></a>
## Configuration

### Keymap

```json
{ "keys": ["alt+shift+t"], "command": "markdown_table_creator" }
```

### Customization

```
{

  // This will be used to align the column when alignment is not specified with ":"
  // Can be "left" / "right" / "center"
  "default_alignment": "left",

  // Each of the characters will be used to separate header line together with "|"
  "extra_header_separators": "",

  // Each of the characters will be used to separate content lines together with "|"
  "extra_content_separators": "",

  // Enabling debug_mode will print errors after the selected text  
  "debug_mode": false,

}
```
