"""Generated from Smithy shape ``com.amazonaws.wafv2#LogType``."""

from typing import Literal, TypeAlias, cast

LogType: TypeAlias = Literal["WAF_LOGS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogType:
    return cast(LogType, data)
