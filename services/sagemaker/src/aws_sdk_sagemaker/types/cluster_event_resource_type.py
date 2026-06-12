"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterEventResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterEventResourceType: TypeAlias = Literal[
    "Cluster",
    "InstanceGroup",
    "Instance",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Cluster",
        "InstanceGroup",
        "Instance",
    )
)


def serialize_aws_json_1_1(value: ClusterEventResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterEventResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterEventResourceType value: {data!r}")
    return cast(ClusterEventResourceType, data)
