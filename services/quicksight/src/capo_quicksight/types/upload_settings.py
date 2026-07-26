"""Generated from Smithy shape ``com.amazonaws.quicksight#UploadSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.delimiter
    import capo_quicksight.types.file_format
    import capo_quicksight.types.positive_integer
    import capo_quicksight.types.string
    import capo_quicksight.types.text_qualifier


class UploadSettings(TypedDict, closed=True):
    format: NotRequired["capo_quicksight.types.file_format.FileFormat"]
    """<p>File format.</p>"""
    start_from_row: NotRequired[
        "capo_quicksight.types.positive_integer.PositiveInteger"
    ]
    """<p>A row number to start reading data from.</p>"""
    contains_header: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>Whether the file has a header row, or the files each have a header row.</p>"""
    text_qualifier: NotRequired["capo_quicksight.types.text_qualifier.TextQualifier"]
    """<p>Text qualifier.</p>"""
    delimiter: NotRequired["capo_quicksight.types.delimiter.Delimiter"]
    """<p>The delimiter between values in the file.</p>"""
    custom_cell_address_range: NotRequired["capo_quicksight.types.string.String"]
    """<p>A custom cell address range for Excel files, specifying which cells to import from the spreadsheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UploadSettings) -> dict:
    out: dict = {}
    if "format" in value:
        import capo_quicksight.types.file_format

        out["Format"] = capo_quicksight.types.file_format.serialize_json(
            value["format"]
        )
    if "start_from_row" in value:
        out["StartFromRow"] = value["start_from_row"]
    if "contains_header" in value:
        out["ContainsHeader"] = value["contains_header"]
    if "text_qualifier" in value:
        import capo_quicksight.types.text_qualifier

        out["TextQualifier"] = capo_quicksight.types.text_qualifier.serialize_json(
            value["text_qualifier"]
        )
    if "delimiter" in value:
        out["Delimiter"] = value["delimiter"]
    if "custom_cell_address_range" in value:
        out["CustomCellAddressRange"] = value["custom_cell_address_range"]
    return out


def deserialize_json(data: dict) -> UploadSettings:
    out: UploadSettings = {}  # type: ignore[typeddict-item]
    if "Format" in data:
        import capo_quicksight.types.file_format

        out["format"] = capo_quicksight.types.file_format.deserialize_json(
            data["Format"]
        )
    if "StartFromRow" in data:
        out["start_from_row"] = data["StartFromRow"]
    if "ContainsHeader" in data:
        out["contains_header"] = data["ContainsHeader"]
    if "TextQualifier" in data:
        import capo_quicksight.types.text_qualifier

        out["text_qualifier"] = capo_quicksight.types.text_qualifier.deserialize_json(
            data["TextQualifier"]
        )
    if "Delimiter" in data:
        out["delimiter"] = data["Delimiter"]
    if "CustomCellAddressRange" in data:
        out["custom_cell_address_range"] = data["CustomCellAddressRange"]
    return out
