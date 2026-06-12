"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#HealthState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_global_accelerator.errors import DeserializationError

HealthState: TypeAlias = Literal[
    "INITIAL",
    "HEALTHY",
    "UNHEALTHY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIAL",
        "HEALTHY",
        "UNHEALTHY",
    )
)


def serialize_aws_json_1_1(value: HealthState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HealthState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HealthState value: {data!r}")
    return cast(HealthState, data)
