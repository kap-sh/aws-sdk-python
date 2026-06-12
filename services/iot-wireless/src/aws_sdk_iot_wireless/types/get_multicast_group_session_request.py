"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetMulticastGroupSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.multicast_group_id


class GetMulticastGroupSessionRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.multicast_group_id.MulticastGroupId"


# --- restJson1 ser/de ---
def serialize_json(value: GetMulticastGroupSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMulticastGroupSessionRequest:
    out: GetMulticastGroupSessionRequest = {}  # type: ignore[typeddict-item]
    return out
