"""Generated from Smithy shape ``com.amazonaws.lakeformation#FilterConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.filter_condition

FilterConditionList: TypeAlias = list[
    "aws_sdk_lakeformation.types.filter_condition.FilterCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterConditionList) -> list:
    import aws_sdk_lakeformation.types.filter_condition

    out: list = []
    for item in value:
        out.append(aws_sdk_lakeformation.types.filter_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterConditionList:
    import aws_sdk_lakeformation.types.filter_condition

    out: FilterConditionList = []
    for item in data:
        out.append(aws_sdk_lakeformation.types.filter_condition.deserialize_json(item))
    return out
