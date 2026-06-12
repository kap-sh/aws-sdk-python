"""Generated from Smithy shape ``com.amazonaws.support#SupportedLanguagesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_support.types.supported_language

SupportedLanguagesList: TypeAlias = list[
    "aws_sdk_support.types.supported_language.SupportedLanguage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedLanguagesList) -> list:
    import aws_sdk_support.types.supported_language

    out: list = []
    for item in value:
        out.append(
            aws_sdk_support.types.supported_language.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SupportedLanguagesList:
    import aws_sdk_support.types.supported_language

    out: SupportedLanguagesList = []
    for item in data:
        out.append(
            aws_sdk_support.types.supported_language.deserialize_aws_json_1_1(item)
        )
    return out
