"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controlcatalog.types.control_mapping

ControlMappings: TypeAlias = list[
    "capo_controlcatalog.types.control_mapping.ControlMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlMappings) -> list:
    import capo_controlcatalog.types.control_mapping

    out: list = []
    for item in value:
        out.append(capo_controlcatalog.types.control_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlMappings:
    import capo_controlcatalog.types.control_mapping

    out: ControlMappings = []
    for item in data:
        out.append(capo_controlcatalog.types.control_mapping.deserialize_json(item))
    return out
