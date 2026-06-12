"""Generated from Smithy shape ``com.amazonaws.fsx#LustreAccessAuditLogLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

LustreAccessAuditLogLevel: TypeAlias = Literal[
    "DISABLED",
    "WARN_ONLY",
    "ERROR_ONLY",
    "WARN_ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "WARN_ONLY",
        "ERROR_ONLY",
        "WARN_ERROR",
    )
)


def serialize_aws_json_1_1(value: LustreAccessAuditLogLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LustreAccessAuditLogLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LustreAccessAuditLogLevel value: {data!r}")
    return cast(LustreAccessAuditLogLevel, data)
