"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#FailoverMode``."""

from typing import Literal, TypeAlias, cast

FailoverMode: TypeAlias = Literal[
    "AUTOMATIC",
    "NO_FAILOVER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FailoverMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FailoverMode:
    return cast(FailoverMode, data)
