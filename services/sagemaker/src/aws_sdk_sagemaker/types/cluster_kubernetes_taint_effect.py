"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterKubernetesTaintEffect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterKubernetesTaintEffect: TypeAlias = Literal[
    "NoSchedule",
    "PreferNoSchedule",
    "NoExecute",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NoSchedule",
        "PreferNoSchedule",
        "NoExecute",
    )
)


def serialize_aws_json_1_1(value: ClusterKubernetesTaintEffect) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterKubernetesTaintEffect:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ClusterKubernetesTaintEffect value: {data!r}"
        )
    return cast(ClusterKubernetesTaintEffect, data)
