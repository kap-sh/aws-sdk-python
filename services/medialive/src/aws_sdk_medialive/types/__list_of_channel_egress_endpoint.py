"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfChannelEgressEndpoint``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.channel_egress_endpoint

__listOfChannelEgressEndpoint: TypeAlias = list[
    "aws_sdk_medialive.types.channel_egress_endpoint.ChannelEgressEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfChannelEgressEndpoint) -> list:
    import aws_sdk_medialive.types.channel_egress_endpoint

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.channel_egress_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfChannelEgressEndpoint:
    import aws_sdk_medialive.types.channel_egress_endpoint

    out: __listOfChannelEgressEndpoint = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.channel_egress_endpoint.deserialize_json(item)
        )
    return out
