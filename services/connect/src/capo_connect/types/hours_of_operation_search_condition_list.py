"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation_search_criteria

HoursOfOperationSearchConditionList: TypeAlias = list[
    "capo_connect.types.hours_of_operation_search_criteria.HoursOfOperationSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationSearchConditionList) -> list:
    import capo_connect.types.hours_of_operation_search_criteria

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.hours_of_operation_search_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HoursOfOperationSearchConditionList:
    import capo_connect.types.hours_of_operation_search_criteria

    out: HoursOfOperationSearchConditionList = []
    for item in data:
        out.append(
            capo_connect.types.hours_of_operation_search_criteria.deserialize_json(item)
        )
    return out
