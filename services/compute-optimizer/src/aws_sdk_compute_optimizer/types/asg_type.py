"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AsgType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

AsgType: TypeAlias = Literal[
    "SingleInstanceType",
    "MixedInstanceTypes",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SingleInstanceType",
        "MixedInstanceTypes",
    )
)


def serialize_aws_json_1_0(value: AsgType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AsgType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AsgType value: {data!r}")
    return cast(AsgType, data)
