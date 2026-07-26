"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#GetConnectInstanceConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaigns.types.instance_id


class GetConnectInstanceConfigRequest(TypedDict, closed=True):
    connect_instance_id: "capo_connectcampaigns.types.instance_id.InstanceId"


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectInstanceConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectInstanceConfigRequest:
    out: GetConnectInstanceConfigRequest = {}  # type: ignore[typeddict-item]
    return out
