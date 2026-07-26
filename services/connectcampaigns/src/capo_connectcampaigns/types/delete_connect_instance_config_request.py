"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#DeleteConnectInstanceConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaigns.types.instance_id


class DeleteConnectInstanceConfigRequest(TypedDict, closed=True):
    connect_instance_id: "capo_connectcampaigns.types.instance_id.InstanceId"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectInstanceConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConnectInstanceConfigRequest:
    out: DeleteConnectInstanceConfigRequest = {}  # type: ignore[typeddict-item]
    return out
