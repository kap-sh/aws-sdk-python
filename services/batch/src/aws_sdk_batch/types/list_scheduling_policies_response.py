"""Generated from Smithy shape ``com.amazonaws.batch#ListSchedulingPoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.scheduling_policy_listing_detail_list
    import aws_sdk_batch.types.string


class ListSchedulingPoliciesResponse(TypedDict):
    scheduling_policies: NotRequired[
        "aws_sdk_batch.types.scheduling_policy_listing_detail_list.SchedulingPolicyListingDetailList"
    ]
    """<p>A list of scheduling policies that match the request.</p>"""
    next_token: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListSchedulingPolicies</code> request. When the results of a <code>ListSchedulingPolicies</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchedulingPoliciesResponse) -> dict:
    out: dict = {}
    if "scheduling_policies" in value:
        import aws_sdk_batch.types.scheduling_policy_listing_detail_list

        out["schedulingPolicies"] = (
            aws_sdk_batch.types.scheduling_policy_listing_detail_list.serialize_json(
                value["scheduling_policies"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSchedulingPoliciesResponse:
    out: ListSchedulingPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "schedulingPolicies" in data:
        import aws_sdk_batch.types.scheduling_policy_listing_detail_list

        out["scheduling_policies"] = (
            aws_sdk_batch.types.scheduling_policy_listing_detail_list.deserialize_json(
                data["schedulingPolicies"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
