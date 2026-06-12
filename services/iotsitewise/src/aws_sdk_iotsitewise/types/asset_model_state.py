"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

AssetModelState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "PROPAGATING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "PROPAGATING",
        "DELETING",
        "FAILED",
    )
)


def serialize_json(value: AssetModelState) -> str:
    return value


def deserialize_json(data: str) -> AssetModelState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssetModelState value: {data!r}")
    return cast(AssetModelState, data)
