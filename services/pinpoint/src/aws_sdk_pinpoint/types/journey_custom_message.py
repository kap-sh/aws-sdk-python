"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneyCustomMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class JourneyCustomMessage(TypedDict, closed=True):
    data: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The message content that's passed to an AWS Lambda function or to a web hook.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JourneyCustomMessage) -> dict:
    out: dict = {}
    if "data" in value:
        out["Data"] = value["data"]
    return out


def deserialize_json(data: dict) -> JourneyCustomMessage:
    out: JourneyCustomMessage = {}  # type: ignore[typeddict-item]
    if "Data" in data:
        out["data"] = data["Data"]
    return out
