"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

AssetModelType: TypeAlias = Literal[
    "ASSET_MODEL",
    "COMPONENT_MODEL",
    "INTERFACE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSET_MODEL",
        "COMPONENT_MODEL",
        "INTERFACE",
    )
)


def serialize_json(value: AssetModelType) -> str:
    return value


def deserialize_json(data: str) -> AssetModelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssetModelType value: {data!r}")
    return cast(AssetModelType, data)
