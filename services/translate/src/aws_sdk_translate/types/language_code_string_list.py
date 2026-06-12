"""Generated from Smithy shape ``com.amazonaws.translate#LanguageCodeStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_translate.types.language_code_string

LanguageCodeStringList: TypeAlias = list[
    "aws_sdk_translate.types.language_code_string.LanguageCodeString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LanguageCodeStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LanguageCodeStringList:
    return list(data)
