"""Generated from Smithy shape ``com.amazonaws.deadline#AcceleratorSelections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.accelerator_selection

AcceleratorSelections: TypeAlias = list[
    "capo_deadline.types.accelerator_selection.AcceleratorSelection"
]


# --- restJson1 ser/de ---
def serialize_json(value: AcceleratorSelections) -> list:
    import capo_deadline.types.accelerator_selection

    out: list = []
    for item in value:
        out.append(capo_deadline.types.accelerator_selection.serialize_json(item))
    return out


def deserialize_json(data: list) -> AcceleratorSelections:
    import capo_deadline.types.accelerator_selection

    out: AcceleratorSelections = []
    for item in data:
        out.append(capo_deadline.types.accelerator_selection.deserialize_json(item))
    return out
