"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ImageStandardGenerativeFieldTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.image_standard_generative_field_type

ImageStandardGenerativeFieldTypes: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.image_standard_generative_field_type.ImageStandardGenerativeFieldType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageStandardGenerativeFieldTypes) -> list:
    import aws_sdk_bedrock_data_automation.types.image_standard_generative_field_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.image_standard_generative_field_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ImageStandardGenerativeFieldTypes:
    import aws_sdk_bedrock_data_automation.types.image_standard_generative_field_type

    out: ImageStandardGenerativeFieldTypes = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.image_standard_generative_field_type.deserialize_json(
                item
            )
        )
    return out
