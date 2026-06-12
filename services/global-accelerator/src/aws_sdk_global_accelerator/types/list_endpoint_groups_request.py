"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListEndpointGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string
    import aws_sdk_global_accelerator.types.max_results


class ListEndpointGroupsRequest(TypedDict):
    listener_arn: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    max_results: NotRequired["aws_sdk_global_accelerator.types.max_results.MaxResults"]
    """<p>The number of endpoint group objects that you want to return with this call. The default value is 10.</p>"""
    next_token: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEndpointGroupsRequest) -> dict:
    out: dict = {}
    out["ListenerArn"] = value["listener_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEndpointGroupsRequest:
    out: ListEndpointGroupsRequest = {}  # type: ignore[typeddict-item]
    if "ListenerArn" in data:
        out["listener_arn"] = data["ListenerArn"]
    else:
        raise DeserializationError("ListEndpointGroupsRequest.listener_arn required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
