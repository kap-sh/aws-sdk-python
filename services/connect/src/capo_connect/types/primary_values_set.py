"""Generated from Smithy shape ``com.amazonaws.connect#PrimaryValuesSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.primary_value

PrimaryValuesSet: TypeAlias = list["capo_connect.types.primary_value.PrimaryValue"]


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryValuesSet) -> list:
    import capo_connect.types.primary_value

    out: list = []
    for item in value:
        out.append(capo_connect.types.primary_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> PrimaryValuesSet:
    import capo_connect.types.primary_value

    out: PrimaryValuesSet = []
    for item in data:
        out.append(capo_connect.types.primary_value.deserialize_json(item))
    return out
