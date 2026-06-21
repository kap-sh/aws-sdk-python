"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ProductCodeType``."""

from typing import Literal, TypeAlias, cast

ProductCodeType: TypeAlias = Literal["marketplace",]


# --- restJson1 ser/de ---
def serialize_json(value: ProductCodeType) -> str:
    return value


def deserialize_json(data: str) -> ProductCodeType:
    return cast(ProductCodeType, data)
