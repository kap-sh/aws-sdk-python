"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DeploymentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

DeploymentType: TypeAlias = Literal[
    "SINGLE_AZ",
    "WITH_MULTIAZ_STANDBY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_AZ",
        "WITH_MULTIAZ_STANDBY",
    )
)


def serialize_aws_json_1_0(value: DeploymentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DeploymentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentType value: {data!r}")
    return cast(DeploymentType, data)
