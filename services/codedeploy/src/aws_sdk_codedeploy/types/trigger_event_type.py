"""Generated from Smithy shape ``com.amazonaws.codedeploy#TriggerEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

TriggerEventType: TypeAlias = Literal[
    "DeploymentStart",
    "DeploymentSuccess",
    "DeploymentFailure",
    "DeploymentStop",
    "DeploymentRollback",
    "DeploymentReady",
    "InstanceStart",
    "InstanceSuccess",
    "InstanceFailure",
    "InstanceReady",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DeploymentStart",
        "DeploymentSuccess",
        "DeploymentFailure",
        "DeploymentStop",
        "DeploymentRollback",
        "DeploymentReady",
        "InstanceStart",
        "InstanceSuccess",
        "InstanceFailure",
        "InstanceReady",
    )
)


def serialize_aws_json_1_1(value: TriggerEventType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TriggerEventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TriggerEventType value: {data!r}")
    return cast(TriggerEventType, data)
