"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationOverrideSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours_of_operation_override_search_criteria

HoursOfOperationOverrideSearchConditionList: TypeAlias = list[
    "aws_sdk_connect.types.hours_of_operation_override_search_criteria.HoursOfOperationOverrideSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationOverrideSearchConditionList) -> list:
    import aws_sdk_connect.types.hours_of_operation_override_search_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.hours_of_operation_override_search_criteria.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HoursOfOperationOverrideSearchConditionList:
    import aws_sdk_connect.types.hours_of_operation_override_search_criteria

    out: HoursOfOperationOverrideSearchConditionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.hours_of_operation_override_search_criteria.deserialize_json(
                item
            )
        )
    return out
