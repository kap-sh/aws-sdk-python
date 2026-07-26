"""Generated from Smithy shape ``com.amazonaws.iotwireless#SendDataToMulticastGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.multicast_group_message_id


class SendDataToMulticastGroupResponse(TypedDict, closed=True):
    message_id: NotRequired[
        "capo_iot_wireless.types.multicast_group_message_id.MulticastGroupMessageId"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SendDataToMulticastGroupResponse) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    return out


def deserialize_json(data: dict) -> SendDataToMulticastGroupResponse:
    out: SendDataToMulticastGroupResponse = {}  # type: ignore[typeddict-item]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    return out
