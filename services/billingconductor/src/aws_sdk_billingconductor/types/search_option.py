"""Generated from Smithy shape ``com.amazonaws.billingconductor#SearchOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

SearchOption: TypeAlias = Literal["STARTS_WITH",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("STARTS_WITH",))


def serialize_json(value: SearchOption) -> str:
    return value


def deserialize_json(data: str) -> SearchOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchOption value: {data!r}")
    return cast(SearchOption, data)
