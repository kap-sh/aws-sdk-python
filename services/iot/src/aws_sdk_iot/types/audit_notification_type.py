"""Generated from Smithy shape ``com.amazonaws.iot#AuditNotificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AuditNotificationType: TypeAlias = Literal["SNS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SNS",))


def serialize_json(value: AuditNotificationType) -> str:
    return value


def deserialize_json(data: str) -> AuditNotificationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuditNotificationType value: {data!r}")
    return cast(AuditNotificationType, data)
