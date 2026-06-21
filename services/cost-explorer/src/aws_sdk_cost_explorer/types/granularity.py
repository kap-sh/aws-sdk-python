"""Generated from Smithy shape ``com.amazonaws.costexplorer#Granularity``."""

from typing import Literal, TypeAlias, cast

Granularity: TypeAlias = Literal[
    "DAILY",
    "MONTHLY",
    "HOURLY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Granularity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Granularity:
    return cast(Granularity, data)
