"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Channels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.channel

Channels: TypeAlias = list["capo_cloudtrail.types.channel.Channel"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Channels) -> list:
    import capo_cloudtrail.types.channel

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.channel.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Channels:
    import capo_cloudtrail.types.channel

    out: Channels = []
    for item in data:
        out.append(capo_cloudtrail.types.channel.deserialize_aws_json_1_1(item))
    return out
