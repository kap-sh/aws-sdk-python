"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceLaunchType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

ECSServiceLaunchType: TypeAlias = Literal[
    "EC2",
    "Fargate",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EC2",
        "Fargate",
    )
)


def serialize_aws_json_1_0(value: ECSServiceLaunchType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ECSServiceLaunchType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ECSServiceLaunchType value: {data!r}")
    return cast(ECSServiceLaunchType, data)
