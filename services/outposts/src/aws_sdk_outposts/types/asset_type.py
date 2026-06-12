"""Generated from Smithy shape ``com.amazonaws.outposts#AssetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

AssetType: TypeAlias = Literal[
    "COMPUTE",
    "STORAGE",
    "POWERSHELF",
    "SWITCH",
    "NETWORKING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPUTE",
        "STORAGE",
        "POWERSHELF",
        "SWITCH",
        "NETWORKING",
    )
)


def serialize_json(value: AssetType) -> str:
    return value


def deserialize_json(data: str) -> AssetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssetType value: {data!r}")
    return cast(AssetType, data)
