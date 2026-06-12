"""Generated from Smithy shape ``com.amazonaws.workdocs#TextLocaleTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.language_code_type

TextLocaleTypeList: TypeAlias = list[
    "aws_sdk_workdocs.types.language_code_type.LanguageCodeType"
]


# --- restJson1 ser/de ---
def serialize_json(value: TextLocaleTypeList) -> list:
    import aws_sdk_workdocs.types.language_code_type

    out: list = []
    for item in value:
        out.append(aws_sdk_workdocs.types.language_code_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> TextLocaleTypeList:
    import aws_sdk_workdocs.types.language_code_type

    out: TextLocaleTypeList = []
    for item in data:
        out.append(aws_sdk_workdocs.types.language_code_type.deserialize_json(item))
    return out
