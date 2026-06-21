"""Generated from Smithy shape ``com.amazonaws.iot#AuditNotificationType``."""

from typing import Literal, TypeAlias, cast

AuditNotificationType: TypeAlias = Literal["SNS",]


# --- restJson1 ser/de ---
def serialize_json(value: AuditNotificationType) -> str:
    return value


def deserialize_json(data: str) -> AuditNotificationType:
    return cast(AuditNotificationType, data)
