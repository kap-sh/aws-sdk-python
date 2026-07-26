"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfChannelEgressEndpoint``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.channel_egress_endpoint

__listOfChannelEgressEndpoint: TypeAlias = list[
    "capo_medialive.types.channel_egress_endpoint.ChannelEgressEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfChannelEgressEndpoint) -> list:
    import capo_medialive.types.channel_egress_endpoint

    out: list = []
    for item in value:
        out.append(capo_medialive.types.channel_egress_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfChannelEgressEndpoint:
    import capo_medialive.types.channel_egress_endpoint

    out: __listOfChannelEgressEndpoint = []
    for item in data:
        out.append(capo_medialive.types.channel_egress_endpoint.deserialize_json(item))
    return out
