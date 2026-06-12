"""Generated from Smithy shape ``com.amazonaws.finspace#KxDeploymentStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

KxDeploymentStrategy: TypeAlias = Literal[
    "NO_RESTART",
    "ROLLING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_RESTART",
        "ROLLING",
    )
)


def serialize_json(value: KxDeploymentStrategy) -> str:
    return value


def deserialize_json(data: str) -> KxDeploymentStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KxDeploymentStrategy value: {data!r}")
    return cast(KxDeploymentStrategy, data)
