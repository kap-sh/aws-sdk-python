"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VideoStandardGenerativeFieldTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.video_standard_generative_field_type

VideoStandardGenerativeFieldTypes: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.video_standard_generative_field_type.VideoStandardGenerativeFieldType"
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoStandardGenerativeFieldTypes) -> list:
    import aws_sdk_bedrock_data_automation.types.video_standard_generative_field_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.video_standard_generative_field_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> VideoStandardGenerativeFieldTypes:
    import aws_sdk_bedrock_data_automation.types.video_standard_generative_field_type

    out: VideoStandardGenerativeFieldTypes = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.video_standard_generative_field_type.deserialize_json(
                item
            )
        )
    return out
