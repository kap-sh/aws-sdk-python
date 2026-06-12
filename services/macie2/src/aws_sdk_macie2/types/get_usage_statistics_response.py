"""Generated from Smithy shape ``com.amazonaws.macie2#GetUsageStatisticsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_usage_record
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.time_range


class GetUsageStatisticsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""
    records: NotRequired[
        "aws_sdk_macie2.types.__list_of_usage_record.__listOfUsageRecord"
    ]
    """<p>An array of objects that contains the results of the query. Each object contains the data for an account that matches the filter criteria specified in the request.</p>"""
    time_range: NotRequired["aws_sdk_macie2.types.time_range.TimeRange"]
    """<p>The inclusive time period that the usage data applies to. Possible values are: MONTH_TO_DATE, for the current calendar month to date; and, PAST_30_DAYS, for the preceding 30 days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsageStatisticsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "records" in value:
        import aws_sdk_macie2.types.__list_of_usage_record

        out["records"] = aws_sdk_macie2.types.__list_of_usage_record.serialize_json(
            value["records"]
        )
    if "time_range" in value:
        import aws_sdk_macie2.types.time_range

        out["timeRange"] = aws_sdk_macie2.types.time_range.serialize_json(
            value["time_range"]
        )
    return out


def deserialize_json(data: dict) -> GetUsageStatisticsResponse:
    out: GetUsageStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "records" in data:
        import aws_sdk_macie2.types.__list_of_usage_record

        out["records"] = aws_sdk_macie2.types.__list_of_usage_record.deserialize_json(
            data["records"]
        )
    if "timeRange" in data:
        import aws_sdk_macie2.types.time_range

        out["time_range"] = aws_sdk_macie2.types.time_range.deserialize_json(
            data["timeRange"]
        )
    return out
