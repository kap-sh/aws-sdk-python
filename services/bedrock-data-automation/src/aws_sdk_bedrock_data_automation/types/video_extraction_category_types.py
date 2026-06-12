"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VideoExtractionCategoryTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.video_extraction_category_type

VideoExtractionCategoryTypes: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.video_extraction_category_type.VideoExtractionCategoryType"
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoExtractionCategoryTypes) -> list:
    import aws_sdk_bedrock_data_automation.types.video_extraction_category_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.video_extraction_category_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> VideoExtractionCategoryTypes:
    import aws_sdk_bedrock_data_automation.types.video_extraction_category_type

    out: VideoExtractionCategoryTypes = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.video_extraction_category_type.deserialize_json(
                item
            )
        )
    return out
