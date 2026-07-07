"""Generated from Smithy shape ``com.amazonaws.pinpoint#CampaignCustomMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class CampaignCustomMessage(TypedDict, closed=True):
    data: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The raw, JSON-formatted string to use as the payload for the message. The maximum size is 5 KB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CampaignCustomMessage) -> dict:
    out: dict = {}
    if "data" in value:
        out["Data"] = value["data"]
    return out


def deserialize_json(data: dict) -> CampaignCustomMessage:
    out: CampaignCustomMessage = {}  # type: ignore[typeddict-item]
    if "Data" in data:
        out["data"] = data["Data"]
    return out
