"""Generated from Smithy shape ``com.amazonaws.quicksight#UploadSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.delimiter
    import aws_sdk_quicksight.types.file_format
    import aws_sdk_quicksight.types.positive_integer
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.text_qualifier


class UploadSettings(TypedDict):
    format: NotRequired["aws_sdk_quicksight.types.file_format.FileFormat"]
    """<p>File format.</p>"""
    start_from_row: NotRequired[
        "aws_sdk_quicksight.types.positive_integer.PositiveInteger"
    ]
    """<p>A row number to start reading data from.</p>"""
    contains_header: NotRequired["aws_sdk_quicksight.types.boolean.Boolean"]
    """<p>Whether the file has a header row, or the files each have a header row.</p>"""
    text_qualifier: NotRequired["aws_sdk_quicksight.types.text_qualifier.TextQualifier"]
    """<p>Text qualifier.</p>"""
    delimiter: NotRequired["aws_sdk_quicksight.types.delimiter.Delimiter"]
    """<p>The delimiter between values in the file.</p>"""
    custom_cell_address_range: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>A custom cell address range for Excel files, specifying which cells to import from the spreadsheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UploadSettings) -> dict:
    out: dict = {}
    if "format" in value:
        import aws_sdk_quicksight.types.file_format

        out["Format"] = aws_sdk_quicksight.types.file_format.serialize_json(
            value["format"]
        )
    if "start_from_row" in value:
        out["StartFromRow"] = value["start_from_row"]
    if "contains_header" in value:
        out["ContainsHeader"] = value["contains_header"]
    if "text_qualifier" in value:
        import aws_sdk_quicksight.types.text_qualifier

        out["TextQualifier"] = aws_sdk_quicksight.types.text_qualifier.serialize_json(
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
        import aws_sdk_quicksight.types.file_format

        out["format"] = aws_sdk_quicksight.types.file_format.deserialize_json(
            data["Format"]
        )
    if "StartFromRow" in data:
        out["start_from_row"] = data["StartFromRow"]
    if "ContainsHeader" in data:
        out["contains_header"] = data["ContainsHeader"]
    if "TextQualifier" in data:
        import aws_sdk_quicksight.types.text_qualifier

        out["text_qualifier"] = (
            aws_sdk_quicksight.types.text_qualifier.deserialize_json(
                data["TextQualifier"]
            )
        )
    if "Delimiter" in data:
        out["delimiter"] = data["Delimiter"]
    if "CustomCellAddressRange" in data:
        out["custom_cell_address_range"] = data["CustomCellAddressRange"]
    return out
