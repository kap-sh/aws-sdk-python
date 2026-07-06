"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListAccessPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.access_policy_type
    import aws_sdk_opensearchserverless.types.resource_filter


class ListAccessPoliciesRequest(TypedDict, closed=True):
    type: "aws_sdk_opensearchserverless.types.access_policy_type.AccessPolicyType"
    """<p>The type of access policy.</p>"""
    resource: NotRequired[
        "aws_sdk_opensearchserverless.types.resource_filter.ResourceFilter"
    ]
    """<p>Resource filters (can be collections or indexes) that policies can apply to.</p>"""
    next_token: NotRequired["str"]
    """<p>If your initial <code>ListAccessPolicies</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListAccessPolicies</code> operations, which returns results in the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAccessPoliciesRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "resource" in value:
        import aws_sdk_opensearchserverless.types.resource_filter

        out["resource"] = (
            aws_sdk_opensearchserverless.types.resource_filter.serialize_aws_json_1_0(
                value["resource"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAccessPoliciesRequest:
    out: ListAccessPoliciesRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("ListAccessPoliciesRequest.type required")
    if "resource" in data:
        import aws_sdk_opensearchserverless.types.resource_filter

        out["resource"] = (
            aws_sdk_opensearchserverless.types.resource_filter.deserialize_aws_json_1_0(
                data["resource"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
