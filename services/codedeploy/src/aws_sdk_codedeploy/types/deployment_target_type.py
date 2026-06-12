"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentTargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

DeploymentTargetType: TypeAlias = Literal[
    "InstanceTarget",
    "LambdaTarget",
    "ECSTarget",
    "CloudFormationTarget",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InstanceTarget",
        "LambdaTarget",
        "ECSTarget",
        "CloudFormationTarget",
    )
)


def serialize_aws_json_1_1(value: DeploymentTargetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentTargetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentTargetType value: {data!r}")
    return cast(DeploymentTargetType, data)
