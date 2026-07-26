"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation

HoursOfOperationList: TypeAlias = list[
    "capo_connect.types.hours_of_operation.HoursOfOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationList) -> list:
    import capo_connect.types.hours_of_operation

    out: list = []
    for item in value:
        out.append(capo_connect.types.hours_of_operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> HoursOfOperationList:
    import capo_connect.types.hours_of_operation

    out: HoursOfOperationList = []
    for item in data:
        out.append(capo_connect.types.hours_of_operation.deserialize_json(item))
    return out
