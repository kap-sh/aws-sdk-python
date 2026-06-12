"""Generated from Smithy shape ``com.amazonaws.xray#InsightCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_xray.errors import DeserializationError

InsightCategory: TypeAlias = Literal["FAULT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FAULT",))


def serialize_json(value: InsightCategory) -> str:
    return value


def deserialize_json(data: str) -> InsightCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightCategory value: {data!r}")
    return cast(InsightCategory, data)
