"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#GetMetricsSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class GetMetricsSummaryRequest(TypedDict, closed=True):
    date: "datetime.datetime"
    """<p>The date you want to retrieve summary metrics from, rounded to the nearest day. The date must be within the past two years.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetricsSummaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMetricsSummaryRequest:
    out: GetMetricsSummaryRequest = {}  # type: ignore[typeddict-item]
    return out
