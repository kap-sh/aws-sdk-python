"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentReadyAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

DeploymentReadyAction: TypeAlias = Literal[
    "CONTINUE_DEPLOYMENT",
    "STOP_DEPLOYMENT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTINUE_DEPLOYMENT",
        "STOP_DEPLOYMENT",
    )
)


def serialize_aws_json_1_1(value: DeploymentReadyAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentReadyAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentReadyAction value: {data!r}")
    return cast(DeploymentReadyAction, data)
