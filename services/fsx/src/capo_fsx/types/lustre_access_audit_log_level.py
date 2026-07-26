"""Generated from Smithy shape ``com.amazonaws.fsx#LustreAccessAuditLogLevel``."""

from typing import Literal, TypeAlias, cast

LustreAccessAuditLogLevel: TypeAlias = Literal[
    "DISABLED",
    "WARN_ONLY",
    "ERROR_ONLY",
    "WARN_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LustreAccessAuditLogLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LustreAccessAuditLogLevel:
    return cast(LustreAccessAuditLogLevel, data)
