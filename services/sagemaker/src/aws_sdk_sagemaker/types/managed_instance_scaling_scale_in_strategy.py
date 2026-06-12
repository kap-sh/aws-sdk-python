"""Generated from Smithy shape ``com.amazonaws.sagemaker#ManagedInstanceScalingScaleInStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ManagedInstanceScalingScaleInStrategy: TypeAlias = Literal[
    "IDLE_RELEASE",
    "CONSOLIDATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IDLE_RELEASE",
        "CONSOLIDATION",
    )
)


def serialize_aws_json_1_1(value: ManagedInstanceScalingScaleInStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedInstanceScalingScaleInStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ManagedInstanceScalingScaleInStrategy value: {data!r}"
        )
    return cast(ManagedInstanceScalingScaleInStrategy, data)
