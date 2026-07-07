"""Generated from Smithy shape ``com.amazonaws.databrew#CsvOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.delimiter
    import aws_sdk_databrew.types.header_row


class CsvOptions(TypedDict, closed=True):
    delimiter: NotRequired["aws_sdk_databrew.types.delimiter.Delimiter"]
    """<p>A single character that specifies the delimiter being used in the CSV file.</p>"""
    header_row: NotRequired["aws_sdk_databrew.types.header_row.HeaderRow"]
    """<p>A variable that specifies whether the first row in the file is parsed as the header. If this value is false, column names are auto-generated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CsvOptions) -> dict:
    out: dict = {}
    if "delimiter" in value:
        out["Delimiter"] = value["delimiter"]
    if "header_row" in value:
        out["HeaderRow"] = value["header_row"]
    return out


def deserialize_json(data: dict) -> CsvOptions:
    out: CsvOptions = {}  # type: ignore[typeddict-item]
    if "Delimiter" in data:
        out["delimiter"] = data["Delimiter"]
    if "HeaderRow" in data:
        out["header_row"] = data["HeaderRow"]
    return out
