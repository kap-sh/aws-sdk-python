"""Generated from Smithy shape ``com.amazonaws.glacier#CSVOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.quote_fields
    import aws_sdk_glacier.types.string


class CSVOutput(TypedDict):
    quote_fields: NotRequired["aws_sdk_glacier.types.quote_fields.QuoteFields"]
    """<p>A value that indicates whether all output fields should be contained within quotation marks.</p>"""
    quote_escape_character: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>A single character used for escaping the quotation-mark character inside an already escaped value.</p>"""
    record_delimiter: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>A value used to separate individual records from each other.</p>"""
    field_delimiter: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>A value used to separate individual fields from each other within a record.</p>"""
    quote_character: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>A value used as an escape character where the field delimiter is part of the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CSVOutput) -> dict:
    out: dict = {}
    if "quote_fields" in value:
        import aws_sdk_glacier.types.quote_fields

        out["QuoteFields"] = aws_sdk_glacier.types.quote_fields.serialize_json(
            value["quote_fields"]
        )
    if "quote_escape_character" in value:
        out["QuoteEscapeCharacter"] = value["quote_escape_character"]
    if "record_delimiter" in value:
        out["RecordDelimiter"] = value["record_delimiter"]
    if "field_delimiter" in value:
        out["FieldDelimiter"] = value["field_delimiter"]
    if "quote_character" in value:
        out["QuoteCharacter"] = value["quote_character"]
    return out


def deserialize_json(data: dict) -> CSVOutput:
    out: CSVOutput = {}  # type: ignore[typeddict-item]
    if "QuoteFields" in data:
        import aws_sdk_glacier.types.quote_fields

        out["quote_fields"] = aws_sdk_glacier.types.quote_fields.deserialize_json(
            data["QuoteFields"]
        )
    if "QuoteEscapeCharacter" in data:
        out["quote_escape_character"] = data["QuoteEscapeCharacter"]
    if "RecordDelimiter" in data:
        out["record_delimiter"] = data["RecordDelimiter"]
    if "FieldDelimiter" in data:
        out["field_delimiter"] = data["FieldDelimiter"]
    if "QuoteCharacter" in data:
        out["quote_character"] = data["QuoteCharacter"]
    return out
