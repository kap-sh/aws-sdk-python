"""Generated from Smithy shape ``com.amazonaws.fsx#WindowsAccessAuditLogLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

WindowsAccessAuditLogLevel: TypeAlias = Literal[
    "DISABLED",
    "SUCCESS_ONLY",
    "FAILURE_ONLY",
    "SUCCESS_AND_FAILURE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "SUCCESS_ONLY",
        "FAILURE_ONLY",
        "SUCCESS_AND_FAILURE",
    )
)


def serialize_aws_json_1_1(value: WindowsAccessAuditLogLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WindowsAccessAuditLogLevel:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WindowsAccessAuditLogLevel value: {data!r}"
        )
    return cast(WindowsAccessAuditLogLevel, data)
