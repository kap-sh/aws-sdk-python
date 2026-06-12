"""Generated from Smithy shape ``com.amazonaws.sagemaker#ManagedInstanceScalingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ManagedInstanceScalingStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: ManagedInstanceScalingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedInstanceScalingStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ManagedInstanceScalingStatus value: {data!r}"
        )
    return cast(ManagedInstanceScalingStatus, data)
