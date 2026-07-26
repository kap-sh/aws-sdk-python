"""Generated from Smithy shape ``com.amazonaws.iot#AuditFindings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.audit_finding

AuditFindings: TypeAlias = list["capo_iot.types.audit_finding.AuditFinding"]


# --- restJson1 ser/de ---
def serialize_json(value: AuditFindings) -> list:
    import capo_iot.types.audit_finding

    out: list = []
    for item in value:
        out.append(capo_iot.types.audit_finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuditFindings:
    import capo_iot.types.audit_finding

    out: AuditFindings = []
    for item in data:
        out.append(capo_iot.types.audit_finding.deserialize_json(item))
    return out
