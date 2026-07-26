"""Generated from Smithy shape ``com.amazonaws.iot#ListBillingGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.billing_group_name_and_arn_list
    import capo_iot.types.next_token


class ListBillingGroupsResponse(TypedDict, closed=True):
    billing_groups: NotRequired[
        "capo_iot.types.billing_group_name_and_arn_list.BillingGroupNameAndArnList"
    ]
    """<p>The list of billing groups.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBillingGroupsResponse) -> dict:
    out: dict = {}
    if "billing_groups" in value:
        import capo_iot.types.billing_group_name_and_arn_list

        out["billingGroups"] = (
            capo_iot.types.billing_group_name_and_arn_list.serialize_json(
                value["billing_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBillingGroupsResponse:
    out: ListBillingGroupsResponse = {}  # type: ignore[typeddict-item]
    if "billingGroups" in data:
        import capo_iot.types.billing_group_name_and_arn_list

        out["billing_groups"] = (
            capo_iot.types.billing_group_name_and_arn_list.deserialize_json(
                data["billingGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
