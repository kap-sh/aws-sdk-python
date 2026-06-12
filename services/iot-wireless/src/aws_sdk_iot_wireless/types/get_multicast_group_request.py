"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetMulticastGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.multicast_group_id


class GetMulticastGroupRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId"


# --- restJson1 ser/de ---
def serialize_json(value: GetMulticastGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMulticastGroupRequest:
    out: GetMulticastGroupRequest = {}  # type: ignore[typeddict-item]
    return out
