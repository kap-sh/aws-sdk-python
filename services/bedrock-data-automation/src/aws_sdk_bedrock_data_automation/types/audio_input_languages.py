"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioInputLanguages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.language

AudioInputLanguages: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.language.Language"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioInputLanguages) -> list:
    import aws_sdk_bedrock_data_automation.types.language

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_data_automation.types.language.serialize_json(item))
    return out


def deserialize_json(data: list) -> AudioInputLanguages:
    import aws_sdk_bedrock_data_automation.types.language

    out: AudioInputLanguages = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.language.deserialize_json(item)
        )
    return out
