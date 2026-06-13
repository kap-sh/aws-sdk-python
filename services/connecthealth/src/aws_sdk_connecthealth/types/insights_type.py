"""Generated from Smithy shape ``com.amazonaws.connecthealth#InsightsType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connecthealth.errors import DeserializationError

InsightsType: TypeAlias = Literal["PRE_VISIT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PRE_VISIT",))


def serialize_json(value: InsightsType) -> str:
    return value


def deserialize_json(data: str) -> InsightsType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightsType value: {data!r}")
    return cast(InsightsType, data)
