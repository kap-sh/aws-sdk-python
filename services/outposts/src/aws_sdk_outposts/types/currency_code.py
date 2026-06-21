"""Generated from Smithy shape ``com.amazonaws.outposts#CurrencyCode``."""

from typing import Literal, TypeAlias, cast

CurrencyCode: TypeAlias = Literal["USD",]


# --- restJson1 ser/de ---
def serialize_json(value: CurrencyCode) -> str:
    return value


def deserialize_json(data: str) -> CurrencyCode:
    return cast(CurrencyCode, data)
