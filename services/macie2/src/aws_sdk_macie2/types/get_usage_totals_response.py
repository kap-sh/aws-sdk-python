"""Generated from Smithy shape ``com.amazonaws.macie2#GetUsageTotalsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_usage_total
    import aws_sdk_macie2.types.time_range


class GetUsageTotalsResponse(TypedDict, closed=True):
    time_range: NotRequired["aws_sdk_macie2.types.time_range.TimeRange"]
    """<p>The inclusive time period that the usage data applies to. Possible values are: MONTH_TO_DATE, for the current calendar month to date; and, PAST_30_DAYS, for the preceding 30 days.</p>"""
    usage_totals: NotRequired[
        "aws_sdk_macie2.types.__list_of_usage_total.__listOfUsageTotal"
    ]
    """<p>An array of objects that contains the results of the query. Each object contains the data for a specific usage metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsageTotalsResponse) -> dict:
    out: dict = {}
    if "time_range" in value:
        import aws_sdk_macie2.types.time_range

        out["timeRange"] = aws_sdk_macie2.types.time_range.serialize_json(
            value["time_range"]
        )
    if "usage_totals" in value:
        import aws_sdk_macie2.types.__list_of_usage_total

        out["usageTotals"] = aws_sdk_macie2.types.__list_of_usage_total.serialize_json(
            value["usage_totals"]
        )
    return out


def deserialize_json(data: dict) -> GetUsageTotalsResponse:
    out: GetUsageTotalsResponse = {}  # type: ignore[typeddict-item]
    if "timeRange" in data:
        import aws_sdk_macie2.types.time_range

        out["time_range"] = aws_sdk_macie2.types.time_range.deserialize_json(
            data["timeRange"]
        )
    if "usageTotals" in data:
        import aws_sdk_macie2.types.__list_of_usage_total

        out["usage_totals"] = (
            aws_sdk_macie2.types.__list_of_usage_total.deserialize_json(
                data["usageTotals"]
            )
        )
    return out
