"""Generated from Smithy shape ``com.amazonaws.iotwireless#CancelMulticastGroupSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.multicast_group_id


class CancelMulticastGroupSessionRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId"


# --- restJson1 ser/de ---
def serialize_json(value: CancelMulticastGroupSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelMulticastGroupSessionRequest:
    out: CancelMulticastGroupSessionRequest = {}  # type: ignore[typeddict-item]
    return out
