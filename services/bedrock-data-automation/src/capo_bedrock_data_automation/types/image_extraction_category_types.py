"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ImageExtractionCategoryTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.image_extraction_category_type

ImageExtractionCategoryTypes: TypeAlias = list[
    "capo_bedrock_data_automation.types.image_extraction_category_type.ImageExtractionCategoryType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageExtractionCategoryTypes) -> list:
    import capo_bedrock_data_automation.types.image_extraction_category_type

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.image_extraction_category_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ImageExtractionCategoryTypes:
    import capo_bedrock_data_automation.types.image_extraction_category_type

    out: ImageExtractionCategoryTypes = []
    for item in data:
        out.append(
            capo_bedrock_data_automation.types.image_extraction_category_type.deserialize_json(
                item
            )
        )
    return out
