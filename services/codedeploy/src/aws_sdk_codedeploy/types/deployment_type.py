"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

DeploymentType: TypeAlias = Literal[
    "IN_PLACE",
    "BLUE_GREEN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PLACE",
        "BLUE_GREEN",
    )
)


def serialize_aws_json_1_1(value: DeploymentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentType value: {data!r}")
    return cast(DeploymentType, data)
