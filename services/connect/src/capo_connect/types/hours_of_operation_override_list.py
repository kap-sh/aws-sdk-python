"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation_override

HoursOfOperationOverrideList: TypeAlias = list[
    "capo_connect.types.hours_of_operation_override.HoursOfOperationOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationOverrideList) -> list:
    import capo_connect.types.hours_of_operation_override

    out: list = []
    for item in value:
        out.append(capo_connect.types.hours_of_operation_override.serialize_json(item))
    return out


def deserialize_json(data: list) -> HoursOfOperationOverrideList:
    import capo_connect.types.hours_of_operation_override

    out: HoursOfOperationOverrideList = []
    for item in data:
        out.append(
            capo_connect.types.hours_of_operation_override.deserialize_json(item)
        )
    return out
