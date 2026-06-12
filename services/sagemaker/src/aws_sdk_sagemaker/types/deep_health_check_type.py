"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeepHealthCheckType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

DeepHealthCheckType: TypeAlias = Literal[
    "InstanceStress",
    "InstanceConnectivity",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InstanceStress",
        "InstanceConnectivity",
    )
)


def serialize_aws_json_1_1(value: DeepHealthCheckType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeepHealthCheckType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeepHealthCheckType value: {data!r}")
    return cast(DeepHealthCheckType, data)
