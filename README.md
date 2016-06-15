# alfred-linguee
An Alfred workflow that helps you faster translate phrases in Linguee.

Features autocomplete, relying on Google Suggest.

## How-to:
The scheme of the query is very simple and uses the following pattern:

`ling <from language ISO 639-1 code><to language ISO 639-1 code> <phrase to translate>`

Which gives us in the real world:

`ling fren le meilleur des deux mondes`

###Note:
* Please keep in mind that the origin and destination languages are mandatory for now and to omit them would lead to weird results.
* The order of the ISO codes has no incidence on the translation as Linguee automatically finds out about the origin and destination languages.

## Getting started:
Download [the latest version](https://github.com/Performat/alfred-linguee/releases/latest). </br></br>

Below are the supported languages and their corresponding ISO 639-1 code:

| Language   | ISO 639-1 code |
|------------|:---:|
| Chinese    | zh |
| Czech      | cz |
| Danish     | da |
| Dutch      | nl |
| English    | en |
| Estonian   | et |
| Finnish    | fi |
| French     | fr |
| German     | de |
| Greek      | el |
| Hungarian  | hu |
| Italian    | it |
| Japanese   | ja |
| Latvian    | lv |
| Lithuanian | lt |
| Maltese    | mt |
| Polish     | pl |
| Portuguese | pt |
| Romanian   | ro |
| Russian    | ru |
| Slovene    | sk |
| Spanish    | es |
| Swedish    | sv |


##To do:
* Add support for default origin and destination languages
