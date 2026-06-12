"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ElasticChannelConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.maximum_sub_channels
    import aws_sdk_chime_sdk_messaging.types.minimum_membership_percentage
    import aws_sdk_chime_sdk_messaging.types.target_memberships_per_sub_channel


class ElasticChannelConfiguration(TypedDict):
    maximum_sub_channels: (
        "aws_sdk_chime_sdk_messaging.types.maximum_sub_channels.MaximumSubChannels"
    )
    """<p>The maximum number of SubChannels that you want to allow in the elastic channel.</p>"""
    target_memberships_per_sub_channel: "aws_sdk_chime_sdk_messaging.types.target_memberships_per_sub_channel.TargetMembershipsPerSubChannel"
    """<p>The maximum number of members allowed in a SubChannel.</p>"""
    minimum_membership_percentage: "aws_sdk_chime_sdk_messaging.types.minimum_membership_percentage.MinimumMembershipPercentage"
    """<p>The minimum allowed percentage of TargetMembershipsPerSubChannel users. Ceil of the calculated value is used in balancing members among SubChannels of the elastic channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElasticChannelConfiguration) -> dict:
    out: dict = {}
    out["MaximumSubChannels"] = value["maximum_sub_channels"]
    out["TargetMembershipsPerSubChannel"] = value["target_memberships_per_sub_channel"]
    out["MinimumMembershipPercentage"] = value["minimum_membership_percentage"]
    return out


def deserialize_json(data: dict) -> ElasticChannelConfiguration:
    out: ElasticChannelConfiguration = {}  # type: ignore[typeddict-item]
    if "MaximumSubChannels" in data:
        out["maximum_sub_channels"] = data["MaximumSubChannels"]
    else:
        raise DeserializationError(
            "ElasticChannelConfiguration.maximum_sub_channels required"
        )
    if "TargetMembershipsPerSubChannel" in data:
        out["target_memberships_per_sub_channel"] = data[
            "TargetMembershipsPerSubChannel"
        ]
    else:
        raise DeserializationError(
            "ElasticChannelConfiguration.target_memberships_per_sub_channel required"
        )
    if "MinimumMembershipPercentage" in data:
        out["minimum_membership_percentage"] = data["MinimumMembershipPercentage"]
    else:
        raise DeserializationError(
            "ElasticChannelConfiguration.minimum_membership_percentage required"
        )
    return out
