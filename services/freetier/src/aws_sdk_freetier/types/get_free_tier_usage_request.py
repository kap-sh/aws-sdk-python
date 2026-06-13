"""Generated from Smithy shape ``com.amazonaws.freetier#GetFreeTierUsageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_freetier.types.expression
    import aws_sdk_freetier.types.max_results
    import aws_sdk_freetier.types.next_page_token


class GetFreeTierUsageRequest(TypedDict):
    filter: NotRequired["aws_sdk_freetier.types.expression.Expression"]
    """<p>An expression that specifies the conditions that you want each <code>FreeTierUsage</code> object to meet.</p>"""
    max_results: "aws_sdk_freetier.types.max_results.MaxResults"
    """<p>The maximum number of results to return in the response. <code>MaxResults</code> means that there can be up to the specified number of values, but there might be fewer results based on your filters.</p>"""
    next_token: NotRequired["aws_sdk_freetier.types.next_page_token.NextPageToken"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetFreeTierUsageRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_freetier.types.expression

        out["filter"] = aws_sdk_freetier.types.expression.serialize_aws_json_1_0(
            value["filter"]
        )
    out["maxResults"] = value.get("max_results", 10)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetFreeTierUsageRequest:
    out: GetFreeTierUsageRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_freetier.types.expression

        out["filter"] = aws_sdk_freetier.types.expression.deserialize_aws_json_1_0(
            data["filter"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 10
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
