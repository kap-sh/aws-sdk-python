"""Generated from Smithy shape ``com.amazonaws.macie2#TimeRange``."""

from typing import Literal, TypeAlias, cast

"""<p>An inclusive time period that Amazon Macie usage data applies to. Possible values are:</p>"""
TimeRange: TypeAlias = Literal[
    "MONTH_TO_DATE",
    "PAST_30_DAYS",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeRange) -> str:
    return value


def deserialize_json(data: str) -> TimeRange:
    return cast(TimeRange, data)
