"""Generated from Smithy shape ``com.amazonaws.workdocs#TextLocaleTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.language_code_type

TextLocaleTypeList: TypeAlias = list[
    "capo_workdocs.types.language_code_type.LanguageCodeType"
]


# --- restJson1 ser/de ---
def serialize_json(value: TextLocaleTypeList) -> list:
    import capo_workdocs.types.language_code_type

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.language_code_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> TextLocaleTypeList:
    import capo_workdocs.types.language_code_type

    out: TextLocaleTypeList = []
    for item in data:
        out.append(capo_workdocs.types.language_code_type.deserialize_json(item))
    return out
