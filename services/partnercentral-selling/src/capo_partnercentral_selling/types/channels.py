"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Channels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.channel

Channels: TypeAlias = list["capo_partnercentral_selling.types.channel.Channel"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Channels) -> list:
    import capo_partnercentral_selling.types.channel

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.channel.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Channels:
    import capo_partnercentral_selling.types.channel

    out: Channels = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.channel.deserialize_aws_json_1_0(item)
        )
    return out
