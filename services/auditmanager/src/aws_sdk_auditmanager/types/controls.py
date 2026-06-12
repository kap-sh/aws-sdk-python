"""Generated from Smithy shape ``com.amazonaws.auditmanager#Controls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control

Controls: TypeAlias = list["aws_sdk_auditmanager.types.control.Control"]


# --- restJson1 ser/de ---
def serialize_json(value: Controls) -> list:
    import aws_sdk_auditmanager.types.control

    out: list = []
    for item in value:
        out.append(aws_sdk_auditmanager.types.control.serialize_json(item))
    return out


def deserialize_json(data: list) -> Controls:
    import aws_sdk_auditmanager.types.control

    out: Controls = []
    for item in data:
        out.append(aws_sdk_auditmanager.types.control.deserialize_json(item))
    return out
