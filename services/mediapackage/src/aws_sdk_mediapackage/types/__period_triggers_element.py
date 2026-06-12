"""Generated from Smithy shape ``com.amazonaws.mediapackage#__PeriodTriggersElement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage.errors import DeserializationError

__PeriodTriggersElement: TypeAlias = Literal["ADS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ADS",))


def serialize_json(value: __PeriodTriggersElement) -> str:
    return value


def deserialize_json(data: str) -> __PeriodTriggersElement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown __PeriodTriggersElement value: {data!r}")
    return cast(__PeriodTriggersElement, data)
