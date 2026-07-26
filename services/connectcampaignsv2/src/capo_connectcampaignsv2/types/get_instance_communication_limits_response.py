"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#GetInstanceCommunicationLimitsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.instance_communication_limits_config


class GetInstanceCommunicationLimitsResponse(TypedDict, closed=True):
    communication_limits_config: NotRequired[
        "capo_connectcampaignsv2.types.instance_communication_limits_config.InstanceCommunicationLimitsConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetInstanceCommunicationLimitsResponse) -> dict:
    out: dict = {}
    if "communication_limits_config" in value:
        import capo_connectcampaignsv2.types.instance_communication_limits_config

        out["communicationLimitsConfig"] = (
            capo_connectcampaignsv2.types.instance_communication_limits_config.serialize_json(
                value["communication_limits_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetInstanceCommunicationLimitsResponse:
    out: GetInstanceCommunicationLimitsResponse = {}  # type: ignore[typeddict-item]
    if "communicationLimitsConfig" in data:
        import capo_connectcampaignsv2.types.instance_communication_limits_config

        out["communication_limits_config"] = (
            capo_connectcampaignsv2.types.instance_communication_limits_config.deserialize_json(
                data["communicationLimitsConfig"]
            )
        )
    return out
