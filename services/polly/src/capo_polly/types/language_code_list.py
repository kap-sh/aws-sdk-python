"""Generated from Smithy shape ``com.amazonaws.polly#LanguageCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_polly.types.language_code

LanguageCodeList: TypeAlias = list["capo_polly.types.language_code.LanguageCode"]


# --- restJson1 ser/de ---
def serialize_json(value: LanguageCodeList) -> list:
    import capo_polly.types.language_code

    out: list = []
    for item in value:
        out.append(capo_polly.types.language_code.serialize_json(item))
    return out


def deserialize_json(data: list) -> LanguageCodeList:
    import capo_polly.types.language_code

    out: LanguageCodeList = []
    for item in data:
        out.append(capo_polly.types.language_code.deserialize_json(item))
    return out
