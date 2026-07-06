"""Generated from Smithy shape ``com.amazonaws.pinpoint#SimpleEmailPart``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class SimpleEmailPart(TypedDict, closed=True):
    charset: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The applicable character set for the message content.</p>"""
    data: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The textual data of the message content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SimpleEmailPart) -> dict:
    out: dict = {}
    if "charset" in value:
        out["Charset"] = value["charset"]
    if "data" in value:
        out["Data"] = value["data"]
    return out


def deserialize_json(data: dict) -> SimpleEmailPart:
    out: SimpleEmailPart = {}  # type: ignore[typeddict-item]
    if "Charset" in data:
        out["charset"] = data["Charset"]
    if "Data" in data:
        out["data"] = data["Data"]
    return out
