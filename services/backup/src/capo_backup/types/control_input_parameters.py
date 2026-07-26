"""Generated from Smithy shape ``com.amazonaws.backup#ControlInputParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.control_input_parameter

ControlInputParameters: TypeAlias = list[
    "capo_backup.types.control_input_parameter.ControlInputParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlInputParameters) -> list:
    import capo_backup.types.control_input_parameter

    out: list = []
    for item in value:
        out.append(capo_backup.types.control_input_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlInputParameters:
    import capo_backup.types.control_input_parameter

    out: ControlInputParameters = []
    for item in data:
        out.append(capo_backup.types.control_input_parameter.deserialize_json(item))
    return out
