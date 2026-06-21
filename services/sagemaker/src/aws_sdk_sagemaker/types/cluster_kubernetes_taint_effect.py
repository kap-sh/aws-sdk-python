"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterKubernetesTaintEffect``."""

from typing import Literal, TypeAlias, cast

ClusterKubernetesTaintEffect: TypeAlias = Literal[
    "NoSchedule",
    "PreferNoSchedule",
    "NoExecute",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterKubernetesTaintEffect) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterKubernetesTaintEffect:
    return cast(ClusterKubernetesTaintEffect, data)
