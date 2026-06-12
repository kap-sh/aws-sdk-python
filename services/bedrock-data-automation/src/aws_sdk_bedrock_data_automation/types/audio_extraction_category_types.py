"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioExtractionCategoryTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.audio_extraction_category_type

AudioExtractionCategoryTypes: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.audio_extraction_category_type.AudioExtractionCategoryType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioExtractionCategoryTypes) -> list:
    import aws_sdk_bedrock_data_automation.types.audio_extraction_category_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.audio_extraction_category_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AudioExtractionCategoryTypes:
    import aws_sdk_bedrock_data_automation.types.audio_extraction_category_type

    out: AudioExtractionCategoryTypes = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.audio_extraction_category_type.deserialize_json(
                item
            )
        )
    return out
