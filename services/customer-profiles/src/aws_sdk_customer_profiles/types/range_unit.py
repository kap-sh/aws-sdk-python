"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RangeUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

RangeUnit: TypeAlias = Literal["DAYS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DAYS",))


def serialize_json(value: RangeUnit) -> str:
    return value


def deserialize_json(data: str) -> RangeUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RangeUnit value: {data!r}")
    return cast(RangeUnit, data)
