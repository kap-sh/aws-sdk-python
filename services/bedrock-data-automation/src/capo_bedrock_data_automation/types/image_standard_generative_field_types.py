"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ImageStandardGenerativeFieldTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.image_standard_generative_field_type

ImageStandardGenerativeFieldTypes: TypeAlias = list[
    "capo_bedrock_data_automation.types.image_standard_generative_field_type.ImageStandardGenerativeFieldType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageStandardGenerativeFieldTypes) -> list:
    import capo_bedrock_data_automation.types.image_standard_generative_field_type

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.image_standard_generative_field_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ImageStandardGenerativeFieldTypes:
    import capo_bedrock_data_automation.types.image_standard_generative_field_type

    out: ImageStandardGenerativeFieldTypes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_data_automation.types.image_standard_generative_field_type.deserialize_json(
                item
            )
        )
    return out
