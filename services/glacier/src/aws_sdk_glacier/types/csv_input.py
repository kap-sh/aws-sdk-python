"""Generated from Smithy shape ``com.amazonaws.glacier#CSVInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.file_header_info
    import aws_sdk_glacier.types.string


class CSVInput(TypedDict):
    file_header_info: NotRequired[
        "aws_sdk_glacier.types.file_header_info.FileHeaderInfo"
    ]
    """<p>Describes the first line of input. Valid values are <code>None</code>, <code>Ignore</code>, and <code>Use</code>.</p>"""
    comments: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>A single character used to indicate that a row should be ignored when the character is present at the start of that row.</p>"""
    quote_escape_character: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>A single character used for escaping the quotation-mark character inside an already escaped value.</p>"""
    record_delimiter: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>A value used to separate individual records from each other.</p>"""
    field_delimiter: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>A value used to separate individual fields from each other within a record.</p>"""
    quote_character: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>A value used as an escape character where the field delimiter is part of the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CSVInput) -> dict:
    out: dict = {}
    if "file_header_info" in value:
        import aws_sdk_glacier.types.file_header_info

        out["FileHeaderInfo"] = aws_sdk_glacier.types.file_header_info.serialize_json(
            value["file_header_info"]
        )
    if "comments" in value:
        out["Comments"] = value["comments"]
    if "quote_escape_character" in value:
        out["QuoteEscapeCharacter"] = value["quote_escape_character"]
    if "record_delimiter" in value:
        out["RecordDelimiter"] = value["record_delimiter"]
    if "field_delimiter" in value:
        out["FieldDelimiter"] = value["field_delimiter"]
    if "quote_character" in value:
        out["QuoteCharacter"] = value["quote_character"]
    return out


def deserialize_json(data: dict) -> CSVInput:
    out: CSVInput = {}  # type: ignore[typeddict-item]
    if "FileHeaderInfo" in data:
        import aws_sdk_glacier.types.file_header_info

        out["file_header_info"] = (
            aws_sdk_glacier.types.file_header_info.deserialize_json(
                data["FileHeaderInfo"]
            )
        )
    if "Comments" in data:
        out["comments"] = data["Comments"]
    if "QuoteEscapeCharacter" in data:
        out["quote_escape_character"] = data["QuoteEscapeCharacter"]
    if "RecordDelimiter" in data:
        out["record_delimiter"] = data["RecordDelimiter"]
    if "FieldDelimiter" in data:
        out["field_delimiter"] = data["FieldDelimiter"]
    if "QuoteCharacter" in data:
        out["quote_character"] = data["QuoteCharacter"]
    return out
