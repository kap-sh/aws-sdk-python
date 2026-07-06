"""Generated from Smithy shape ``com.amazonaws.macie2#GetUsageTotalsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class GetUsageTotalsRequest(TypedDict, closed=True):
    time_range: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The inclusive time period to retrieve the data for. Valid values are: MONTH_TO_DATE, for the current calendar month to date; and, PAST_30_DAYS, for the preceding 30 days. If you don't specify a value for this parameter, Amazon Macie provides aggregated usage data for the preceding 30 days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsageTotalsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUsageTotalsRequest:
    out: GetUsageTotalsRequest = {}  # type: ignore[typeddict-item]
    return out
