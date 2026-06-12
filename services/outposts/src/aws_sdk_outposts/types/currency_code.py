"""Generated from Smithy shape ``com.amazonaws.outposts#CurrencyCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

CurrencyCode: TypeAlias = Literal["USD",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("USD",))


def serialize_json(value: CurrencyCode) -> str:
    return value


def deserialize_json(data: str) -> CurrencyCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CurrencyCode value: {data!r}")
    return cast(CurrencyCode, data)
