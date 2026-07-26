"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchContentCategoryTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.content_category_type

SearchContentCategoryTypeList: TypeAlias = list[
    "capo_workdocs.types.content_category_type.ContentCategoryType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchContentCategoryTypeList) -> list:
    import capo_workdocs.types.content_category_type

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.content_category_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchContentCategoryTypeList:
    import capo_workdocs.types.content_category_type

    out: SearchContentCategoryTypeList = []
    for item in data:
        out.append(capo_workdocs.types.content_category_type.deserialize_json(item))
    return out
