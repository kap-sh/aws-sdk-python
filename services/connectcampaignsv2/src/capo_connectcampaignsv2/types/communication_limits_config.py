"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CommunicationLimitsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.communication_limits
    import capo_connectcampaignsv2.types.instance_limits_handling


class CommunicationLimitsConfig(TypedDict, closed=True):
    all_channel_subtypes: NotRequired[
        "capo_connectcampaignsv2.types.communication_limits.CommunicationLimits"
    ]
    instance_limits_handling: NotRequired[
        "capo_connectcampaignsv2.types.instance_limits_handling.InstanceLimitsHandling"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CommunicationLimitsConfig) -> dict:
    out: dict = {}
    if "all_channel_subtypes" in value:
        import capo_connectcampaignsv2.types.communication_limits

        out["allChannelSubtypes"] = (
            capo_connectcampaignsv2.types.communication_limits.serialize_json(
                value["all_channel_subtypes"]
            )
        )
    if "instance_limits_handling" in value:
        out["instanceLimitsHandling"] = value["instance_limits_handling"]
    return out


def deserialize_json(data: dict) -> CommunicationLimitsConfig:
    out: CommunicationLimitsConfig = {}  # type: ignore[typeddict-item]
    if "allChannelSubtypes" in data:
        import capo_connectcampaignsv2.types.communication_limits

        out["all_channel_subtypes"] = (
            capo_connectcampaignsv2.types.communication_limits.deserialize_json(
                data["allChannelSubtypes"]
            )
        )
    if "instanceLimitsHandling" in data:
        out["instance_limits_handling"] = data["instanceLimitsHandling"]
    return out
