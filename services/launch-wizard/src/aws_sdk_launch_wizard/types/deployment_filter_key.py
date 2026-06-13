"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_launch_wizard.errors import DeserializationError

DeploymentFilterKey: TypeAlias = Literal[
    "WORKLOAD_NAME",
    "DEPLOYMENT_STATUS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WORKLOAD_NAME",
        "DEPLOYMENT_STATUS",
    )
)


def serialize_json(value: DeploymentFilterKey) -> str:
    return value


def deserialize_json(data: str) -> DeploymentFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentFilterKey value: {data!r}")
    return cast(DeploymentFilterKey, data)
