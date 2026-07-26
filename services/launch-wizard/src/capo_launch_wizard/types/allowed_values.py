"""Generated from Smithy shape ``com.amazonaws.launchwizard#AllowedValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_launch_wizard.types.value_string

AllowedValues: TypeAlias = list["capo_launch_wizard.types.value_string.ValueString"]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedValues) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedValues:
    return list(data)
