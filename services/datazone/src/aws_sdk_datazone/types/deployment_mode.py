"""Generated from Smithy shape ``com.amazonaws.datazone#DeploymentMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

DeploymentMode: TypeAlias = Literal[
    "ON_CREATE",
    "ON_DEMAND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_CREATE",
        "ON_DEMAND",
    )
)


def serialize_json(value: DeploymentMode) -> str:
    return value


def deserialize_json(data: str) -> DeploymentMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentMode value: {data!r}")
    return cast(DeploymentMode, data)
