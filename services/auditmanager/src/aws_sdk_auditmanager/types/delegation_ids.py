"""Generated from Smithy shape ``com.amazonaws.auditmanager#DelegationIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.uuid

DelegationIds: TypeAlias = list["aws_sdk_auditmanager.types.uuid.UUID"]


# --- restJson1 ser/de ---
def serialize_json(value: DelegationIds) -> list:
    return list(value)


def deserialize_json(data: list) -> DelegationIds:
    return list(data)
