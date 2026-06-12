"""Generated from Smithy shape ``com.amazonaws.iotwireless#SendDataToMulticastGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.multicast_group_message_id


class SendDataToMulticastGroupResponse(TypedDict):
    message_id: NotRequired[
        "aws_sdk_iot_wireless.types.multicast_group_message_id.MulticastGroupMessageId"
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
