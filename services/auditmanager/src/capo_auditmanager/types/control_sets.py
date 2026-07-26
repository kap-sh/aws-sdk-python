"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.control_set

ControlSets: TypeAlias = list["capo_auditmanager.types.control_set.ControlSet"]


# --- restJson1 ser/de ---
def serialize_json(value: ControlSets) -> list:
    import capo_auditmanager.types.control_set

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.control_set.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlSets:
    import capo_auditmanager.types.control_set

    out: ControlSets = []
    for item in data:
        out.append(capo_auditmanager.types.control_set.deserialize_json(item))
    return out
