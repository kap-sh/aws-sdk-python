"""Generated from Smithy shape ``com.amazonaws.auditmanager#ExportDestinationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

ExportDestinationType: TypeAlias = Literal["S3",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("S3",))


def serialize_json(value: ExportDestinationType) -> str:
    return value


def deserialize_json(data: str) -> ExportDestinationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportDestinationType value: {data!r}")
    return cast(ExportDestinationType, data)
