"""Generated from Smithy shape ``com.amazonaws.xray#InsightCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.insight_category

InsightCategoryList: TypeAlias = list[
    "aws_sdk_xray.types.insight_category.InsightCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightCategoryList) -> list:
    import aws_sdk_xray.types.insight_category

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.insight_category.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightCategoryList:
    import aws_sdk_xray.types.insight_category

    out: InsightCategoryList = []
    for item in data:
        out.append(aws_sdk_xray.types.insight_category.deserialize_json(item))
    return out
