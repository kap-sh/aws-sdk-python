"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CategoryNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.category_name

CategoryNameList: TypeAlias = list[
    "aws_sdk_chime_sdk_media_pipelines.types.category_name.CategoryName"
]


# --- restJson1 ser/de ---
def serialize_json(value: CategoryNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> CategoryNameList:
    return list(data)
