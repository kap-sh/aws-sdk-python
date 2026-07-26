"""Generated from Smithy shape ``com.amazonaws.support#SupportedLanguagesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_support.types.supported_language

SupportedLanguagesList: TypeAlias = list[
    "capo_support.types.supported_language.SupportedLanguage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedLanguagesList) -> list:
    import capo_support.types.supported_language

    out: list = []
    for item in value:
        out.append(capo_support.types.supported_language.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SupportedLanguagesList:
    import capo_support.types.supported_language

    out: SupportedLanguagesList = []
    for item in data:
        out.append(capo_support.types.supported_language.deserialize_aws_json_1_1(item))
    return out
