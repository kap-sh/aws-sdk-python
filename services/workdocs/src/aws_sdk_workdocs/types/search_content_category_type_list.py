"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchContentCategoryTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.content_category_type

SearchContentCategoryTypeList: TypeAlias = list[
    "aws_sdk_workdocs.types.content_category_type.ContentCategoryType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchContentCategoryTypeList) -> list:
    import aws_sdk_workdocs.types.content_category_type

    out: list = []
    for item in value:
        out.append(aws_sdk_workdocs.types.content_category_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchContentCategoryTypeList:
    import aws_sdk_workdocs.types.content_category_type

    out: SearchContentCategoryTypeList = []
    for item in data:
        out.append(aws_sdk_workdocs.types.content_category_type.deserialize_json(item))
    return out
