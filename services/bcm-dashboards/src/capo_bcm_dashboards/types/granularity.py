"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#Granularity``."""

from typing import Literal, TypeAlias, cast

Granularity: TypeAlias = Literal[
    "HOURLY",
    "DAILY",
    "MONTHLY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Granularity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Granularity:
    return cast(Granularity, data)
