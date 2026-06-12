"""Generated from Smithy shape ``com.amazonaws.rbin#RetentionPeriodUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rbin.errors import DeserializationError

RetentionPeriodUnit: TypeAlias = Literal["DAYS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DAYS",))


def serialize_json(value: RetentionPeriodUnit) -> str:
    return value


def deserialize_json(data: str) -> RetentionPeriodUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetentionPeriodUnit value: {data!r}")
    return cast(RetentionPeriodUnit, data)
