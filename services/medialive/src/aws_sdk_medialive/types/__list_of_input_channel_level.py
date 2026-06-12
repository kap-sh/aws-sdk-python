"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputChannelLevel``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_channel_level

__listOfInputChannelLevel: TypeAlias = list[
    "aws_sdk_medialive.types.input_channel_level.InputChannelLevel"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputChannelLevel) -> list:
    import aws_sdk_medialive.types.input_channel_level

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.input_channel_level.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputChannelLevel:
    import aws_sdk_medialive.types.input_channel_level

    out: __listOfInputChannelLevel = []
    for item in data:
        out.append(aws_sdk_medialive.types.input_channel_level.deserialize_json(item))
    return out
