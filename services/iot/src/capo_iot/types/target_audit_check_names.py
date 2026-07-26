"""Generated from Smithy shape ``com.amazonaws.iot#TargetAuditCheckNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.audit_check_name

TargetAuditCheckNames: TypeAlias = list[
    "capo_iot.types.audit_check_name.AuditCheckName"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetAuditCheckNames) -> list:
    return list(value)


def deserialize_json(data: list) -> TargetAuditCheckNames:
    return list(data)
