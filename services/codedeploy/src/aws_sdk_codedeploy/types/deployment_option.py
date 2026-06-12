"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

DeploymentOption: TypeAlias = Literal[
    "WITH_TRAFFIC_CONTROL",
    "WITHOUT_TRAFFIC_CONTROL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WITH_TRAFFIC_CONTROL",
        "WITHOUT_TRAFFIC_CONTROL",
    )
)


def serialize_aws_json_1_1(value: DeploymentOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentOption value: {data!r}")
    return cast(DeploymentOption, data)
