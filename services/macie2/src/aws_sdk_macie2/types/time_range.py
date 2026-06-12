"""Generated from Smithy shape ``com.amazonaws.macie2#TimeRange``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>An inclusive time period that Amazon Macie usage data applies to. Possible values are:</p>"""
TimeRange: TypeAlias = Literal[
    "MONTH_TO_DATE",
    "PAST_30_DAYS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MONTH_TO_DATE",
        "PAST_30_DAYS",
    )
)


def serialize_json(value: TimeRange) -> str:
    return value


def deserialize_json(data: str) -> TimeRange:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeRange value: {data!r}")
    return cast(TimeRange, data)
