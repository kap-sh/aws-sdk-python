"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentWaitType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

DeploymentWaitType: TypeAlias = Literal[
    "READY_WAIT",
    "TERMINATION_WAIT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY_WAIT",
        "TERMINATION_WAIT",
    )
)


def serialize_aws_json_1_1(value: DeploymentWaitType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentWaitType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentWaitType value: {data!r}")
    return cast(DeploymentWaitType, data)
