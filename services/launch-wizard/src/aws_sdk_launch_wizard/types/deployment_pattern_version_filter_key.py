"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentPatternVersionFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_launch_wizard.errors import DeserializationError

DeploymentPatternVersionFilterKey: TypeAlias = Literal["updateFromVersion",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("updateFromVersion",))


def serialize_json(value: DeploymentPatternVersionFilterKey) -> str:
    return value


def deserialize_json(data: str) -> DeploymentPatternVersionFilterKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeploymentPatternVersionFilterKey value: {data!r}"
        )
    return cast(DeploymentPatternVersionFilterKey, data)
