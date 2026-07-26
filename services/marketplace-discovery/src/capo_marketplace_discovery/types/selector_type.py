"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SelectorType``."""

from typing import Literal, TypeAlias, cast

SelectorType: TypeAlias = Literal["Duration",]


# --- restJson1 ser/de ---
def serialize_json(value: SelectorType) -> str:
    return value


def deserialize_json(data: str) -> SelectorType:
    return cast(SelectorType, data)
