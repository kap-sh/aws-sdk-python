"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisPostContactSummaryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

RealTimeContactAnalysisPostContactSummaryStatus: TypeAlias = Literal[
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "COMPLETED",
    )
)


def serialize_json(value: RealTimeContactAnalysisPostContactSummaryStatus) -> str:
    return value


def deserialize_json(data: str) -> RealTimeContactAnalysisPostContactSummaryStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RealTimeContactAnalysisPostContactSummaryStatus value: {data!r}"
        )
    return cast(RealTimeContactAnalysisPostContactSummaryStatus, data)
