"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ClusterDeploymentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

ClusterDeploymentType: TypeAlias = Literal["MULTI_NODE_READ_REPLICAS",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("MULTI_NODE_READ_REPLICAS",))


def serialize_aws_json_1_0(value: ClusterDeploymentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ClusterDeploymentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterDeploymentType value: {data!r}")
    return cast(ClusterDeploymentType, data)
