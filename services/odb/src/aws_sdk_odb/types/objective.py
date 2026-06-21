"""Generated from Smithy shape ``com.amazonaws.odb#Objective``."""

from typing import Literal, TypeAlias, cast

Objective: TypeAlias = Literal[
    "AUTO",
    "BALANCED",
    "BASIC",
    "HIGH_THROUGHPUT",
    "LOW_LATENCY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Objective) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Objective:
    return cast(Objective, data)
