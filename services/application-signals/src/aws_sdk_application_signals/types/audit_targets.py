"""Generated from Smithy shape ``com.amazonaws.applicationsignals#AuditTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.audit_target

AuditTargets: TypeAlias = list[
    "aws_sdk_application_signals.types.audit_target.AuditTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditTargets) -> list:
    import aws_sdk_application_signals.types.audit_target

    out: list = []
    for item in value:
        out.append(aws_sdk_application_signals.types.audit_target.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuditTargets:
    import aws_sdk_application_signals.types.audit_target

    out: AuditTargets = []
    for item in data:
        out.append(
            aws_sdk_application_signals.types.audit_target.deserialize_json(item)
        )
    return out
