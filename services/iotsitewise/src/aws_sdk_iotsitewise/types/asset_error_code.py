"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

AssetErrorCode: TypeAlias = Literal["INTERNAL_FAILURE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INTERNAL_FAILURE",))


def serialize_json(value: AssetErrorCode) -> str:
    return value


def deserialize_json(data: str) -> AssetErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssetErrorCode value: {data!r}")
    return cast(AssetErrorCode, data)
