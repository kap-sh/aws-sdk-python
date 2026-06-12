"""Generated from Smithy shape ``com.amazonaws.appconfig#DeploymentState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appconfig.errors import DeserializationError

DeploymentState: TypeAlias = Literal[
    "BAKING",
    "VALIDATING",
    "DEPLOYING",
    "COMPLETE",
    "ROLLING_BACK",
    "ROLLED_BACK",
    "REVERTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BAKING",
        "VALIDATING",
        "DEPLOYING",
        "COMPLETE",
        "ROLLING_BACK",
        "ROLLED_BACK",
        "REVERTED",
    )
)


def serialize_json(value: DeploymentState) -> str:
    return value


def deserialize_json(data: str) -> DeploymentState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentState value: {data!r}")
    return cast(DeploymentState, data)
