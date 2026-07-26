"""Generated from Smithy shape ``com.amazonaws.connect#EffectiveHoursOfOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.effective_hours_of_operations

EffectiveHoursOfOperationList: TypeAlias = list[
    "capo_connect.types.effective_hours_of_operations.EffectiveHoursOfOperations"
]


# --- restJson1 ser/de ---
def serialize_json(value: EffectiveHoursOfOperationList) -> list:
    import capo_connect.types.effective_hours_of_operations

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.effective_hours_of_operations.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EffectiveHoursOfOperationList:
    import capo_connect.types.effective_hours_of_operations

    out: EffectiveHoursOfOperationList = []
    for item in data:
        out.append(
            capo_connect.types.effective_hours_of_operations.deserialize_json(item)
        )
    return out
