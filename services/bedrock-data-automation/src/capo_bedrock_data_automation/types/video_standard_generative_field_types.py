"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VideoStandardGenerativeFieldTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.video_standard_generative_field_type

VideoStandardGenerativeFieldTypes: TypeAlias = list[
    "capo_bedrock_data_automation.types.video_standard_generative_field_type.VideoStandardGenerativeFieldType"
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoStandardGenerativeFieldTypes) -> list:
    import capo_bedrock_data_automation.types.video_standard_generative_field_type

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.video_standard_generative_field_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> VideoStandardGenerativeFieldTypes:
    import capo_bedrock_data_automation.types.video_standard_generative_field_type

    out: VideoStandardGenerativeFieldTypes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_data_automation.types.video_standard_generative_field_type.deserialize_json(
                item
            )
        )
    return out
