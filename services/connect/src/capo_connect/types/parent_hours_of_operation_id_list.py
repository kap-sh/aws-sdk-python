"""Generated from Smithy shape ``com.amazonaws.connect#ParentHoursOfOperationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation_id

ParentHoursOfOperationIdList: TypeAlias = list[
    "capo_connect.types.hours_of_operation_id.HoursOfOperationId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParentHoursOfOperationIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ParentHoursOfOperationIdList:
    return list(data)
