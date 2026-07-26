"""Generated from Smithy shape ``com.amazonaws.fsx#WindowsAccessAuditLogLevel``."""

from typing import Literal, TypeAlias, cast

WindowsAccessAuditLogLevel: TypeAlias = Literal[
    "DISABLED",
    "SUCCESS_ONLY",
    "FAILURE_ONLY",
    "SUCCESS_AND_FAILURE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WindowsAccessAuditLogLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WindowsAccessAuditLogLevel:
    return cast(WindowsAccessAuditLogLevel, data)
