"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#InstanceCommunicationLimitsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.communication_limits


class InstanceCommunicationLimitsConfig(TypedDict, closed=True):
    all_channel_subtypes: NotRequired[
        "capo_connectcampaignsv2.types.communication_limits.CommunicationLimits"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceCommunicationLimitsConfig) -> dict:
    out: dict = {}
    if "all_channel_subtypes" in value:
        import capo_connectcampaignsv2.types.communication_limits

        out["allChannelSubtypes"] = (
            capo_connectcampaignsv2.types.communication_limits.serialize_json(
                value["all_channel_subtypes"]
            )
        )
    return out


def deserialize_json(data: dict) -> InstanceCommunicationLimitsConfig:
    out: InstanceCommunicationLimitsConfig = {}  # type: ignore[typeddict-item]
    if "allChannelSubtypes" in data:
        import capo_connectcampaignsv2.types.communication_limits

        out["all_channel_subtypes"] = (
            capo_connectcampaignsv2.types.communication_limits.deserialize_json(
                data["allChannelSubtypes"]
            )
        )
    return out
