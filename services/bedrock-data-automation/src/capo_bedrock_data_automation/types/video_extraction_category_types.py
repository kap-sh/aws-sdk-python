"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VideoExtractionCategoryTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.video_extraction_category_type

VideoExtractionCategoryTypes: TypeAlias = list[
    "capo_bedrock_data_automation.types.video_extraction_category_type.VideoExtractionCategoryType"
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoExtractionCategoryTypes) -> list:
    import capo_bedrock_data_automation.types.video_extraction_category_type

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.video_extraction_category_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> VideoExtractionCategoryTypes:
    import capo_bedrock_data_automation.types.video_extraction_category_type

    out: VideoExtractionCategoryTypes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_data_automation.types.video_extraction_category_type.deserialize_json(
                item
            )
        )
    return out
