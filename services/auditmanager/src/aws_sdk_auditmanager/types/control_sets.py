"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_set

ControlSets: TypeAlias = list["aws_sdk_auditmanager.types.control_set.ControlSet"]


# --- restJson1 ser/de ---
def serialize_json(value: ControlSets) -> list:
    import aws_sdk_auditmanager.types.control_set

    out: list = []
    for item in value:
        out.append(aws_sdk_auditmanager.types.control_set.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlSets:
    import aws_sdk_auditmanager.types.control_set

    out: ControlSets = []
    for item in data:
        out.append(aws_sdk_auditmanager.types.control_set.deserialize_json(item))
    return out
