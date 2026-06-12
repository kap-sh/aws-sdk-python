"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Idle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

Idle: TypeAlias = Literal[
    "True",
    "False",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "True",
        "False",
    )
)


def serialize_aws_json_1_0(value: Idle) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Idle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Idle value: {data!r}")
    return cast(Idle, data)
