"""Generated from Smithy shape ``com.amazonaws.deadline#AcceleratorTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.accelerator_type

AcceleratorTypes: TypeAlias = list[
    "capo_deadline.types.accelerator_type.AcceleratorType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AcceleratorTypes) -> list:
    import capo_deadline.types.accelerator_type

    out: list = []
    for item in value:
        out.append(capo_deadline.types.accelerator_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> AcceleratorTypes:
    import capo_deadline.types.accelerator_type

    out: AcceleratorTypes = []
    for item in data:
        out.append(capo_deadline.types.accelerator_type.deserialize_json(item))
    return out
