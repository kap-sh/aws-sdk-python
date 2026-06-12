"""Generated from Smithy shape ``com.amazonaws.translate#TextTranslationJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_translate.types.text_translation_job_properties

TextTranslationJobPropertiesList: TypeAlias = list[
    "aws_sdk_translate.types.text_translation_job_properties.TextTranslationJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextTranslationJobPropertiesList) -> list:
    import aws_sdk_translate.types.text_translation_job_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_translate.types.text_translation_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TextTranslationJobPropertiesList:
    import aws_sdk_translate.types.text_translation_job_properties

    out: TextTranslationJobPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_translate.types.text_translation_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
