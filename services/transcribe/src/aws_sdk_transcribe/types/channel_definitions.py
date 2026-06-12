"""Generated from Smithy shape ``com.amazonaws.transcribe#ChannelDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.channel_definition

ChannelDefinitions: TypeAlias = list[
    "aws_sdk_transcribe.types.channel_definition.ChannelDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelDefinitions) -> list:
    import aws_sdk_transcribe.types.channel_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transcribe.types.channel_definition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ChannelDefinitions:
    import aws_sdk_transcribe.types.channel_definition

    out: ChannelDefinitions = []
    for item in data:
        out.append(
            aws_sdk_transcribe.types.channel_definition.deserialize_aws_json_1_1(item)
        )
    return out
