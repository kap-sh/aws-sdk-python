"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterAutoScalingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterAutoScalingMode: TypeAlias = Literal[
    "Enable",
    "Disable",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enable",
        "Disable",
    )
)


def serialize_aws_json_1_1(value: ClusterAutoScalingMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterAutoScalingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterAutoScalingMode value: {data!r}")
    return cast(ClusterAutoScalingMode, data)
