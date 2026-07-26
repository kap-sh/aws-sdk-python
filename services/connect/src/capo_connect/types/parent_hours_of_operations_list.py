"""Generated from Smithy shape ``com.amazonaws.connect#ParentHoursOfOperationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operations_identifier

ParentHoursOfOperationsList: TypeAlias = list[
    "capo_connect.types.hours_of_operations_identifier.HoursOfOperationsIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParentHoursOfOperationsList) -> list:
    import capo_connect.types.hours_of_operations_identifier

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.hours_of_operations_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ParentHoursOfOperationsList:
    import capo_connect.types.hours_of_operations_identifier

    out: ParentHoursOfOperationsList = []
    for item in data:
        out.append(
            capo_connect.types.hours_of_operations_identifier.deserialize_json(item)
        )
    return out
