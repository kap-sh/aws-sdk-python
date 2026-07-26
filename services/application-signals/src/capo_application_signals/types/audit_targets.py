"""Generated from Smithy shape ``com.amazonaws.applicationsignals#AuditTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.audit_target

AuditTargets: TypeAlias = list[
    "capo_application_signals.types.audit_target.AuditTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditTargets) -> list:
    import capo_application_signals.types.audit_target

    out: list = []
    for item in value:
        out.append(capo_application_signals.types.audit_target.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuditTargets:
    import capo_application_signals.types.audit_target

    out: AuditTargets = []
    for item in data:
        out.append(capo_application_signals.types.audit_target.deserialize_json(item))
    return out
