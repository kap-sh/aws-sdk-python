"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSDeploymentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

OpenZFSDeploymentType: TypeAlias = Literal[
    "SINGLE_AZ_1",
    "SINGLE_AZ_2",
    "SINGLE_AZ_HA_1",
    "SINGLE_AZ_HA_2",
    "MULTI_AZ_1",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_AZ_1",
        "SINGLE_AZ_2",
        "SINGLE_AZ_HA_1",
        "SINGLE_AZ_HA_2",
        "MULTI_AZ_1",
    )
)


def serialize_aws_json_1_1(value: OpenZFSDeploymentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpenZFSDeploymentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpenZFSDeploymentType value: {data!r}")
    return cast(OpenZFSDeploymentType, data)
