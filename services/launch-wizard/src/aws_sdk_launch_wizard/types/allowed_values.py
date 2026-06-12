"""Generated from Smithy shape ``com.amazonaws.launchwizard#AllowedValues``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.value_string

AllowedValues: TypeAlias = list["aws_sdk_launch_wizard.types.value_string.ValueString"]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedValues) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedValues:
    return list(data)