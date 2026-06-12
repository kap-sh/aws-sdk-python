"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeAggregationAuthorizationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.limit
    import aws_sdk_config_service.types.string


class DescribeAggregationAuthorizationsRequest(TypedDict):
    limit: "aws_sdk_config_service.types.limit.Limit"
    """<p>The maximum number of AggregationAuthorizations returned on each page. The default is maximum. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAggregationAuthorizationsRequest) -> dict:
    out: dict = {}
    out["Limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAggregationAuthorizationsRequest:
    out: DescribeAggregationAuthorizationsRequest = {}  # type: ignore[typeddict-item]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
