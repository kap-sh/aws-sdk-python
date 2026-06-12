"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioStandardGenerativeFieldTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.audio_standard_generative_field_type

AudioStandardGenerativeFieldTypes: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.audio_standard_generative_field_type.AudioStandardGenerativeFieldType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioStandardGenerativeFieldTypes) -> list:
    import aws_sdk_bedrock_data_automation.types.audio_standard_generative_field_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.audio_standard_generative_field_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AudioStandardGenerativeFieldTypes:
    import aws_sdk_bedrock_data_automation.types.audio_standard_generative_field_type

    out: AudioStandardGenerativeFieldTypes = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.audio_standard_generative_field_type.deserialize_json(
                item
            )
        )
    return out
