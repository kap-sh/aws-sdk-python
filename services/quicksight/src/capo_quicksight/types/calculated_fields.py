"""Generated from Smithy shape ``com.amazonaws.quicksight#CalculatedFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.calculated_field

CalculatedFields: TypeAlias = list[
    "capo_quicksight.types.calculated_field.CalculatedField"
]


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedFields) -> list:
    import capo_quicksight.types.calculated_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.calculated_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> CalculatedFields:
    import capo_quicksight.types.calculated_field

    out: CalculatedFields = []
    for item in data:
        out.append(capo_quicksight.types.calculated_field.deserialize_json(item))
    return out
