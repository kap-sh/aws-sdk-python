"""Generated from Smithy shape ``com.amazonaws.configservice#DescribePendingAggregationRequestsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.describe_pending_aggregation_requests_limit
    import aws_sdk_config_service.types.string


class DescribePendingAggregationRequestsRequest(TypedDict, closed=True):
    limit: "aws_sdk_config_service.types.describe_pending_aggregation_requests_limit.DescribePendingAggregationRequestsLimit"
    """<p>The maximum number of evaluation results returned on each page. The default is maximum. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePendingAggregationRequestsRequest) -> dict:
    out: dict = {}
    out["Limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePendingAggregationRequestsRequest:
    out: DescribePendingAggregationRequestsRequest = {}  # type: ignore[typeddict-item]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
