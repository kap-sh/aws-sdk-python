"""Generated from Smithy shape ``com.amazonaws.translate#LanguagesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_translate.types.language

LanguagesList: TypeAlias = list["capo_translate.types.language.Language"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LanguagesList) -> list:
    import capo_translate.types.language

    out: list = []
    for item in value:
        out.append(capo_translate.types.language.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LanguagesList:
    import capo_translate.types.language

    out: LanguagesList = []
    for item in data:
        out.append(capo_translate.types.language.deserialize_aws_json_1_1(item))
    return out
