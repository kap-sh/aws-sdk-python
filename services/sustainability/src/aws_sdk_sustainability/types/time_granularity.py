"""Generated from Smithy shape ``com.amazonaws.sustainability#TimeGranularity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sustainability.errors import DeserializationError

"""<p>Specifies the time period over which emissions data is aggregated.</p>"""
TimeGranularity: TypeAlias = Literal[
    "YEARLY_CALENDAR",
    "YEARLY_FISCAL",
    "QUARTERLY_CALENDAR",
    "QUARTERLY_FISCAL",
    "MONTHLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "YEARLY_CALENDAR",
        "YEARLY_FISCAL",
        "QUARTERLY_CALENDAR",
        "QUARTERLY_FISCAL",
        "MONTHLY",
    )
)


def serialize_json(value: TimeGranularity) -> str:
    return value


def deserialize_json(data: str) -> TimeGranularity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeGranularity value: {data!r}")
    return cast(TimeGranularity, data)
