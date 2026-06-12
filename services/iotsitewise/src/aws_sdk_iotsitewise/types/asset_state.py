"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

AssetState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "FAILED",
    )
)


def serialize_json(value: AssetState) -> str:
    return value


def deserialize_json(data: str) -> AssetState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssetState value: {data!r}")
    return cast(AssetState, data)
