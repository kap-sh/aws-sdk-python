"""Generated from Smithy shape ``com.amazonaws.billingconductor#LineItemFilterValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

LineItemFilterValue: TypeAlias = Literal["SAVINGS_PLAN_NEGATION",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SAVINGS_PLAN_NEGATION",))


def serialize_json(value: LineItemFilterValue) -> str:
    return value


def deserialize_json(data: str) -> LineItemFilterValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LineItemFilterValue value: {data!r}")
    return cast(LineItemFilterValue, data)
