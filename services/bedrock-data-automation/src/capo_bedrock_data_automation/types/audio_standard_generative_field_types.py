"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioStandardGenerativeFieldTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.audio_standard_generative_field_type

AudioStandardGenerativeFieldTypes: TypeAlias = list[
    "capo_bedrock_data_automation.types.audio_standard_generative_field_type.AudioStandardGenerativeFieldType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioStandardGenerativeFieldTypes) -> list:
    import capo_bedrock_data_automation.types.audio_standard_generative_field_type

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.audio_standard_generative_field_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AudioStandardGenerativeFieldTypes:
    import capo_bedrock_data_automation.types.audio_standard_generative_field_type

    out: AudioStandardGenerativeFieldTypes = []
    for item in data:
        out.append(
            capo_bedrock_data_automation.types.audio_standard_generative_field_type.deserialize_json(
                item
            )
        )
    return out
