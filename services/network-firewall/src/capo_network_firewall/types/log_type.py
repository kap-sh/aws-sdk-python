"""Generated from Smithy shape ``com.amazonaws.networkfirewall#LogType``."""

from typing import Literal, TypeAlias, cast

LogType: TypeAlias = Literal[
    "ALERT",
    "FLOW",
    "TLS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LogType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LogType:
    return cast(LogType, data)
