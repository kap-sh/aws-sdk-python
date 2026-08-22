"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioExtractionCategoryTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.audio_extraction_category_type

AudioExtractionCategoryTypes: TypeAlias = list[
    "capo_bedrock_data_automation.types.audio_extraction_category_type.AudioExtractionCategoryType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioExtractionCategoryTypes) -> list:
    import capo_bedrock_data_automation.types.audio_extraction_category_type

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.audio_extraction_category_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AudioExtractionCategoryTypes:
    import capo_bedrock_data_automation.types.audio_extraction_category_type

    out: AudioExtractionCategoryTypes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_data_automation.types.audio_extraction_category_type.deserialize_json(
                item
            )
        )
    return out
