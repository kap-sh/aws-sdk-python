"""Generated from Smithy shape ``com.amazonaws.chime#CreateMeetingDialOutResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.guid_string


class CreateMeetingDialOutResponse(TypedDict):
    transaction_id: NotRequired["aws_sdk_chime.types.guid_string.GuidString"]
    """<p>Unique ID that tracks API calls.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMeetingDialOutResponse) -> dict:
    out: dict = {}
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    return out


def deserialize_json(data: dict) -> CreateMeetingDialOutResponse:
    out: CreateMeetingDialOutResponse = {}  # type: ignore[typeddict-item]
    if "TransactionId" in data:
        out["transaction_id"] = data["TransactionId"]
    return out
