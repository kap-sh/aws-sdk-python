"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#DeleteConnectInstanceConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_deletion_policy
    import aws_sdk_connectcampaignsv2.types.instance_id


class DeleteConnectInstanceConfigRequest(TypedDict):
    connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId"
    campaign_deletion_policy: NotRequired[
        "aws_sdk_connectcampaignsv2.types.campaign_deletion_policy.CampaignDeletionPolicy"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectInstanceConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConnectInstanceConfigRequest:
    out: DeleteConnectInstanceConfigRequest = {}  # type: ignore[typeddict-item]
    return out
