"""Generated from Smithy shape ``com.amazonaws.securityhub#DateRangeUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

DateRangeUnit: TypeAlias = Literal["DAYS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DAYS",))


def serialize_json(value: DateRangeUnit) -> str:
    return value


def deserialize_json(data: str) -> DateRangeUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DateRangeUnit value: {data!r}")
    return cast(DateRangeUnit, data)
