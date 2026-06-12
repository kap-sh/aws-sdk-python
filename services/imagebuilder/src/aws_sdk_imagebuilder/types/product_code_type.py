"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ProductCodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

ProductCodeType: TypeAlias = Literal["marketplace",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("marketplace",))


def serialize_json(value: ProductCodeType) -> str:
    return value


def deserialize_json(data: str) -> ProductCodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProductCodeType value: {data!r}")
    return cast(ProductCodeType, data)
