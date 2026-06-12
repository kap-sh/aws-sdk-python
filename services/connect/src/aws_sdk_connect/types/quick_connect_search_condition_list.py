"""Generated from Smithy shape ``com.amazonaws.connect#QuickConnectSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.quick_connect_search_criteria

QuickConnectSearchConditionList: TypeAlias = list[
    "aws_sdk_connect.types.quick_connect_search_criteria.QuickConnectSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickConnectSearchConditionList) -> list:
    import aws_sdk_connect.types.quick_connect_search_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.quick_connect_search_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> QuickConnectSearchConditionList:
    import aws_sdk_connect.types.quick_connect_search_criteria

    out: QuickConnectSearchConditionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.quick_connect_search_criteria.deserialize_json(item)
        )
    return out
