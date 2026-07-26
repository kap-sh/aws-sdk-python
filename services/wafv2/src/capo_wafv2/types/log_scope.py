"""Generated from Smithy shape ``com.amazonaws.wafv2#LogScope``."""

from typing import Literal, TypeAlias, cast

LogScope: TypeAlias = Literal[
    "CUSTOMER",
    "SECURITY_LAKE",
    "CLOUDWATCH_TELEMETRY_RULE_MANAGED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogScope:
    return cast(LogScope, data)
