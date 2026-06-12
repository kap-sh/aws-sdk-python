"""Generated from Smithy shape ``com.amazonaws.finspace#KxClusterCodeDeploymentStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

KxClusterCodeDeploymentStrategy: TypeAlias = Literal[
    "NO_RESTART",
    "ROLLING",
    "FORCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_RESTART",
        "ROLLING",
        "FORCE",
    )
)


def serialize_json(value: KxClusterCodeDeploymentStrategy) -> str:
    return value


def deserialize_json(data: str) -> KxClusterCodeDeploymentStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown KxClusterCodeDeploymentStrategy value: {data!r}"
        )
    return cast(KxClusterCodeDeploymentStrategy, data)
