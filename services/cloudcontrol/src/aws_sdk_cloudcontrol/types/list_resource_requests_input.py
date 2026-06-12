"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ListResourceRequestsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.max_results
    import aws_sdk_cloudcontrol.types.next_token
    import aws_sdk_cloudcontrol.types.resource_request_status_filter


class ListResourceRequestsInput(TypedDict):
    max_results: NotRequired["aws_sdk_cloudcontrol.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p> <p>The default is <code>20</code>.</p>"""
    next_token: NotRequired["aws_sdk_cloudcontrol.types.next_token.NextToken"]
    """<p>If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.</p>"""
    resource_request_status_filter: NotRequired[
        "aws_sdk_cloudcontrol.types.resource_request_status_filter.ResourceRequestStatusFilter"
    ]
    """<p>The filter criteria to apply to the requests returned.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListResourceRequestsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "resource_request_status_filter" in value:
        import aws_sdk_cloudcontrol.types.resource_request_status_filter

        out["ResourceRequestStatusFilter"] = (
            aws_sdk_cloudcontrol.types.resource_request_status_filter.serialize_aws_json_1_0(
                value["resource_request_status_filter"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListResourceRequestsInput:
    out: ListResourceRequestsInput = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ResourceRequestStatusFilter" in data:
        import aws_sdk_cloudcontrol.types.resource_request_status_filter

        out["resource_request_status_filter"] = (
            aws_sdk_cloudcontrol.types.resource_request_status_filter.deserialize_aws_json_1_0(
                data["ResourceRequestStatusFilter"]
            )
        )
    return out
