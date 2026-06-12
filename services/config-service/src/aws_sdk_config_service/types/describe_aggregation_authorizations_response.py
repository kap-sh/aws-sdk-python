"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeAggregationAuthorizationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregation_authorization_list
    import aws_sdk_config_service.types.string


class DescribeAggregationAuthorizationsResponse(TypedDict):
    aggregation_authorizations: NotRequired[
        "aws_sdk_config_service.types.aggregation_authorization_list.AggregationAuthorizationList"
    ]
    """<p>Returns a list of authorizations granted to various aggregator accounts and regions.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAggregationAuthorizationsResponse) -> dict:
    out: dict = {}
    if "aggregation_authorizations" in value:
        import aws_sdk_config_service.types.aggregation_authorization_list

        out["AggregationAuthorizations"] = (
            aws_sdk_config_service.types.aggregation_authorization_list.serialize_aws_json_1_1(
                value["aggregation_authorizations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAggregationAuthorizationsResponse:
    out: DescribeAggregationAuthorizationsResponse = {}  # type: ignore[typeddict-item]
    if "AggregationAuthorizations" in data:
        import aws_sdk_config_service.types.aggregation_authorization_list

        out["aggregation_authorizations"] = (
            aws_sdk_config_service.types.aggregation_authorization_list.deserialize_aws_json_1_1(
                data["AggregationAuthorizations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
