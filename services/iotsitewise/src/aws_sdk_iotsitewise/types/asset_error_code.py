"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetErrorCode``."""

from typing import Literal, TypeAlias, cast

AssetErrorCode: TypeAlias = Literal["INTERNAL_FAILURE",]


# --- restJson1 ser/de ---
def serialize_json(value: AssetErrorCode) -> str:
    return value


def deserialize_json(data: str) -> AssetErrorCode:
    return cast(AssetErrorCode, data)
