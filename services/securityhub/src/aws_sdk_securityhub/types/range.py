"""Generated from Smithy shape ``com.amazonaws.securityhub#Range``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.long


class Range(TypedDict, closed=True):
    start: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p>The number of lines (for a line range) or characters (for an offset range) from the beginning of the file to the end of the sensitive data.</p>"""
    end: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p>The number of lines (for a line range) or characters (for an offset range) from the beginning of the file to the end of the sensitive data.</p>"""
    start_column: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p>In the line where the sensitive data starts, the column within the line where the sensitive data starts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Range) -> dict:
    out: dict = {}
    if "start" in value:
        out["Start"] = value["start"]
    if "end" in value:
        out["End"] = value["end"]
    if "start_column" in value:
        out["StartColumn"] = value["start_column"]
    return out


def deserialize_json(data: dict) -> Range:
    out: Range = {}  # type: ignore[typeddict-item]
    if "Start" in data:
        out["start"] = data["Start"]
    if "End" in data:
        out["end"] = data["End"]
    if "StartColumn" in data:
        out["start_column"] = data["StartColumn"]
    return out
