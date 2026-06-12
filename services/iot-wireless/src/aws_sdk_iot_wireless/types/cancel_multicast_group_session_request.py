"""Generated from Smithy shape ``com.amazonaws.iotwireless#CancelMulticastGroupSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.multicast_group_id


class CancelMulticastGroupSessionRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId"


# --- restJson1 ser/de ---
def serialize_json(value: CancelMulticastGroupSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelMulticastGroupSessionRequest:
    out: CancelMulticastGroupSessionRequest = {}  # type: ignore[typeddict-item]
    return out
