"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#DeleteConnectInstanceConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_deletion_policy
    import capo_connectcampaignsv2.types.instance_id


class DeleteConnectInstanceConfigRequest(TypedDict, closed=True):
    connect_instance_id: "capo_connectcampaignsv2.types.instance_id.InstanceId"
    campaign_deletion_policy: NotRequired[
        "capo_connectcampaignsv2.types.campaign_deletion_policy.CampaignDeletionPolicy"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectInstanceConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConnectInstanceConfigRequest:
    out: DeleteConnectInstanceConfigRequest = {}  # type: ignore[typeddict-item]
    return out
