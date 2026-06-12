"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceIdle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

InstanceIdle: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: InstanceIdle) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceIdle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceIdle value: {data!r}")
    return cast(InstanceIdle, data)
