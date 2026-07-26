"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationOverrideSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation_override_search_criteria

HoursOfOperationOverrideSearchConditionList: TypeAlias = list[
    "capo_connect.types.hours_of_operation_override_search_criteria.HoursOfOperationOverrideSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationOverrideSearchConditionList) -> list:
    import capo_connect.types.hours_of_operation_override_search_criteria

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.hours_of_operation_override_search_criteria.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HoursOfOperationOverrideSearchConditionList:
    import capo_connect.types.hours_of_operation_override_search_criteria

    out: HoursOfOperationOverrideSearchConditionList = []
    for item in data:
        out.append(
            capo_connect.types.hours_of_operation_override_search_criteria.deserialize_json(
                item
            )
        )
    return out
