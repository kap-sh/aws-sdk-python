"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListLifecyclePoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.lifecycle_policy_summaries


class ListLifecyclePoliciesResponse(TypedDict):
    lifecycle_policy_summaries: NotRequired[
        "aws_sdk_opensearchserverless.types.lifecycle_policy_summaries.LifecyclePolicySummaries"
    ]
    """<p>Details about the requested lifecycle policies.</p>"""
    next_token: NotRequired["str"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListLifecyclePoliciesResponse) -> dict:
    out: dict = {}
    if "lifecycle_policy_summaries" in value:
        import aws_sdk_opensearchserverless.types.lifecycle_policy_summaries

        out["lifecyclePolicySummaries"] = (
            aws_sdk_opensearchserverless.types.lifecycle_policy_summaries.serialize_aws_json_1_0(
                value["lifecycle_policy_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListLifecyclePoliciesResponse:
    out: ListLifecyclePoliciesResponse = {}  # type: ignore[typeddict-item]
    if "lifecyclePolicySummaries" in data:
        import aws_sdk_opensearchserverless.types.lifecycle_policy_summaries

        out["lifecycle_policy_summaries"] = (
            aws_sdk_opensearchserverless.types.lifecycle_policy_summaries.deserialize_aws_json_1_0(
                data["lifecyclePolicySummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
