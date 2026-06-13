"""Generated from Smithy shape ``com.amazonaws.odb#Objective``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

Objective: TypeAlias = Literal[
    "AUTO",
    "BALANCED",
    "BASIC",
    "HIGH_THROUGHPUT",
    "LOW_LATENCY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "BALANCED",
        "BASIC",
        "HIGH_THROUGHPUT",
        "LOW_LATENCY",
    )
)


def serialize_aws_json_1_0(value: Objective) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Objective:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Objective value: {data!r}")
    return cast(Objective, data)
