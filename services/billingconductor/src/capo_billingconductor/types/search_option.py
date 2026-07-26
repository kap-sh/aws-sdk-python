"""Generated from Smithy shape ``com.amazonaws.billingconductor#SearchOption``."""

from typing import Literal, TypeAlias, cast

SearchOption: TypeAlias = Literal["STARTS_WITH",]


# --- restJson1 ser/de ---
def serialize_json(value: SearchOption) -> str:
    return value


def deserialize_json(data: str) -> SearchOption:
    return cast(SearchOption, data)
