"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelVersionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

AssetModelVersionType: TypeAlias = Literal[
    "LATEST",
    "ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LATEST",
        "ACTIVE",
    )
)


def serialize_json(value: AssetModelVersionType) -> str:
    return value


def deserialize_json(data: str) -> AssetModelVersionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssetModelVersionType value: {data!r}")
    return cast(AssetModelVersionType, data)
