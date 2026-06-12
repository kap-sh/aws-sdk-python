"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentCreator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

DeploymentCreator: TypeAlias = Literal[
    "user",
    "autoscaling",
    "codeDeployRollback",
    "CodeDeploy",
    "CodeDeployAutoUpdate",
    "CloudFormation",
    "CloudFormationRollback",
    "autoscalingTermination",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "user",
        "autoscaling",
        "codeDeployRollback",
        "CodeDeploy",
        "CodeDeployAutoUpdate",
        "CloudFormation",
        "CloudFormationRollback",
        "autoscalingTermination",
    )
)


def serialize_aws_json_1_1(value: DeploymentCreator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentCreator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentCreator value: {data!r}")
    return cast(DeploymentCreator, data)
