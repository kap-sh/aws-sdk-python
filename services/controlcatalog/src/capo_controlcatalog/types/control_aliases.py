"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlAliases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controlcatalog.types.control_alias

ControlAliases: TypeAlias = list["capo_controlcatalog.types.control_alias.ControlAlias"]


# --- restJson1 ser/de ---
def serialize_json(value: ControlAliases) -> list:
    return list(value)


def deserialize_json(data: list) -> ControlAliases:
    return list(data)
