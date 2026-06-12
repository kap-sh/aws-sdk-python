"""Generated from Smithy shape ``com.amazonaws.auditmanager#Delegations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.delegation

Delegations: TypeAlias = list["aws_sdk_auditmanager.types.delegation.Delegation"]


# --- restJson1 ser/de ---
def serialize_json(value: Delegations) -> list:
    import aws_sdk_auditmanager.types.delegation

    out: list = []
    for item in value:
        out.append(aws_sdk_auditmanager.types.delegation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Delegations:
    import aws_sdk_auditmanager.types.delegation

    out: Delegations = []
    for item in data:
        out.append(aws_sdk_auditmanager.types.delegation.deserialize_json(item))
    return out
