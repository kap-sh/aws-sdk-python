"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ChannelDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.channel_definition

ChannelDefinitions: TypeAlias = list[
    "aws_sdk_transcribe_streaming.types.channel_definition.ChannelDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelDefinitions) -> list:
    import aws_sdk_transcribe_streaming.types.channel_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transcribe_streaming.types.channel_definition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ChannelDefinitions:
    import aws_sdk_transcribe_streaming.types.channel_definition

    out: ChannelDefinitions = []
    for item in data:
        out.append(
            aws_sdk_transcribe_streaming.types.channel_definition.deserialize_json(item)
        )
    return out
