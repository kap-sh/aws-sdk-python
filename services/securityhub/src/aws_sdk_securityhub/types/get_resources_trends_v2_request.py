"""Generated from Smithy shape ``com.amazonaws.securityhub#GetResourcesTrendsV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.resources_trends_filters
    import aws_sdk_securityhub.types.timestamp


class GetResourcesTrendsV2Request(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_securityhub.types.resources_trends_filters.ResourcesTrendsFilters"
    ]
    """<p>The filters to apply to the resources trend data.</p>"""
    start_time: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p>The starting timestamp for the time period to analyze resources trends, in ISO 8601 format.</p>"""
    end_time: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p>The ending timestamp for the time period to analyze resources trends, in ISO 8601 format.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The token to use for paginating results. This value is returned in the response if more results are available.</p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of trend data points to return in a single response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcesTrendsV2Request) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_securityhub.types.resources_trends_filters

        out["Filters"] = (
            aws_sdk_securityhub.types.resources_trends_filters.serialize_json(
                value["filters"]
            )
        )
    if "start_time" in value:
        import aws_sdk_securityhub.types.timestamp

        out["StartTime"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_securityhub.types.timestamp

        out["EndTime"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> GetResourcesTrendsV2Request:
    out: GetResourcesTrendsV2Request = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_securityhub.types.resources_trends_filters

        out["filters"] = (
            aws_sdk_securityhub.types.resources_trends_filters.deserialize_json(
                data["Filters"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_securityhub.types.timestamp

        out["start_time"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_securityhub.types.timestamp

        out["end_time"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["EndTime"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
