"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ListInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.arn
    import aws_sdk_servicediscovery.types.max_results
    import aws_sdk_servicediscovery.types.next_token


class ListInstancesRequest(TypedDict, closed=True):
    service_id: "aws_sdk_servicediscovery.types.arn.Arn"
    r"""<p>The ID or Amazon Resource Name (ARN) of the service that you want to list instances for. For services created in a shared namespace, specify the service ARN. For more information about shared namespaces, see <a href=\"https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html\">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""
    next_token: NotRequired["aws_sdk_servicediscovery.types.next_token.NextToken"]
    """<p>For the first <code>ListInstances</code> request, omit this value.</p> <p>If more than <code>MaxResults</code> instances match the specified criteria, you can submit another <code>ListInstances</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p>"""
    max_results: NotRequired["aws_sdk_servicediscovery.types.max_results.MaxResults"]
    """<p>The maximum number of instances that you want Cloud Map to return in the response to a <code>ListInstances</code> request. If you don't specify a value for <code>MaxResults</code>, Cloud Map returns up to 100 instances.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInstancesRequest) -> dict:
    out: dict = {}
    out["ServiceId"] = value["service_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInstancesRequest:
    out: ListInstancesRequest = {}  # type: ignore[typeddict-item]
    if "ServiceId" in data:
        out["service_id"] = data["ServiceId"]
    else:
        raise DeserializationError("ListInstancesRequest.service_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
