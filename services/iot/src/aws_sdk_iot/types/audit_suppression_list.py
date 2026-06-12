"""Generated from Smithy shape ``com.amazonaws.iot#AuditSuppressionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_suppression

AuditSuppressionList: TypeAlias = list[
    "aws_sdk_iot.types.audit_suppression.AuditSuppression"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditSuppressionList) -> list:
    import aws_sdk_iot.types.audit_suppression

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.audit_suppression.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuditSuppressionList:
    import aws_sdk_iot.types.audit_suppression

    out: AuditSuppressionList = []
    for item in data:
        out.append(aws_sdk_iot.types.audit_suppression.deserialize_json(item))
    return out
