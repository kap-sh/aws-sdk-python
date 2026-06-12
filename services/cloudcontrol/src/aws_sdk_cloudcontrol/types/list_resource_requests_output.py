"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ListResourceRequestsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.next_token
    import aws_sdk_cloudcontrol.types.resource_request_status_summaries


class ListResourceRequestsOutput(TypedDict):
    resource_request_status_summaries: NotRequired[
        "aws_sdk_cloudcontrol.types.resource_request_status_summaries.ResourceRequestStatusSummaries"
    ]
    """<p>The requests that match the specified filter criteria.</p>"""
    next_token: NotRequired["aws_sdk_cloudcontrol.types.next_token.NextToken"]
    """<p>If the request doesn't return all of the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <code>ListResources</code> again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to null.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListResourceRequestsOutput) -> dict:
    out: dict = {}
    if "resource_request_status_summaries" in value:
        import aws_sdk_cloudcontrol.types.resource_request_status_summaries

        out["ResourceRequestStatusSummaries"] = (
            aws_sdk_cloudcontrol.types.resource_request_status_summaries.serialize_aws_json_1_0(
                value["resource_request_status_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListResourceRequestsOutput:
    out: ListResourceRequestsOutput = {}  # type: ignore[typeddict-item]
    if "ResourceRequestStatusSummaries" in data:
        import aws_sdk_cloudcontrol.types.resource_request_status_summaries

        out["resource_request_status_summaries"] = (
            aws_sdk_cloudcontrol.types.resource_request_status_summaries.deserialize_aws_json_1_0(
                data["ResourceRequestStatusSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
