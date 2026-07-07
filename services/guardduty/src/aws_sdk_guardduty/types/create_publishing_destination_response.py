"""Generated from Smithy shape ``com.amazonaws.guardduty#CreatePublishingDestinationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class CreatePublishingDestinationResponse(TypedDict, closed=True):
    destination_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ID of the publishing destination that is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePublishingDestinationResponse) -> dict:
    out: dict = {}
    if "destination_id" in value:
        out["destinationId"] = value["destination_id"]
    return out


def deserialize_json(data: dict) -> CreatePublishingDestinationResponse:
    out: CreatePublishingDestinationResponse = {}  # type: ignore[typeddict-item]
    if "destinationId" in data:
        out["destination_id"] = data["destinationId"]
    return out
