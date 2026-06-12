"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Channels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.channel

Channels: TypeAlias = list["aws_sdk_partnercentral_selling.types.channel.Channel"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Channels) -> list:
    import aws_sdk_partnercentral_selling.types.channel

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.channel.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Channels:
    import aws_sdk_partnercentral_selling.types.channel

    out: Channels = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.channel.deserialize_aws_json_1_0(item)
        )
    return out
