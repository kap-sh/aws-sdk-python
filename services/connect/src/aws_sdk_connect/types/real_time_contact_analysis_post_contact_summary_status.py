"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisPostContactSummaryStatus``."""

from typing import Literal, TypeAlias, cast

RealTimeContactAnalysisPostContactSummaryStatus: TypeAlias = Literal[
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisPostContactSummaryStatus) -> str:
    return value


def deserialize_json(data: str) -> RealTimeContactAnalysisPostContactSummaryStatus:
    return cast(RealTimeContactAnalysisPostContactSummaryStatus, data)
