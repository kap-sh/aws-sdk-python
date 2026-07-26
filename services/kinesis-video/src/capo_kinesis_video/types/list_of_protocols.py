"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ListOfProtocols``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_video.types.channel_protocol

ListOfProtocols: TypeAlias = list[
    "capo_kinesis_video.types.channel_protocol.ChannelProtocol"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfProtocols) -> list:
    import capo_kinesis_video.types.channel_protocol

    out: list = []
    for item in value:
        out.append(capo_kinesis_video.types.channel_protocol.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfProtocols:
    import capo_kinesis_video.types.channel_protocol

    out: ListOfProtocols = []
    for item in data:
        out.append(capo_kinesis_video.types.channel_protocol.deserialize_json(item))
    return out
