"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeploymentFailureHandlingPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

DeploymentFailureHandlingPolicy: TypeAlias = Literal[
    "ROLLBACK",
    "DO_NOTHING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROLLBACK",
        "DO_NOTHING",
    )
)


def serialize_json(value: DeploymentFailureHandlingPolicy) -> str:
    return value


def deserialize_json(data: str) -> DeploymentFailureHandlingPolicy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeploymentFailureHandlingPolicy value: {data!r}"
        )
    return cast(DeploymentFailureHandlingPolicy, data)
