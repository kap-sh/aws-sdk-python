"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CostCurrency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

CostCurrency: TypeAlias = Literal["USD",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("USD",))


def serialize_json(value: CostCurrency) -> str:
    return value


def deserialize_json(data: str) -> CostCurrency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CostCurrency value: {data!r}")
    return cast(CostCurrency, data)
