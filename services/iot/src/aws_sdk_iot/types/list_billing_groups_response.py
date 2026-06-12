"""Generated from Smithy shape ``com.amazonaws.iot#ListBillingGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.billing_group_name_and_arn_list
    import aws_sdk_iot.types.next_token


class ListBillingGroupsResponse(TypedDict):
    billing_groups: NotRequired[
        "aws_sdk_iot.types.billing_group_name_and_arn_list.BillingGroupNameAndArnList"
    ]
    """<p>The list of billing groups.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBillingGroupsResponse) -> dict:
    out: dict = {}
    if "billing_groups" in value:
        import aws_sdk_iot.types.billing_group_name_and_arn_list

        out["billingGroups"] = (
            aws_sdk_iot.types.billing_group_name_and_arn_list.serialize_json(
                value["billing_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBillingGroupsResponse:
    out: ListBillingGroupsResponse = {}  # type: ignore[typeddict-item]
    if "billingGroups" in data:
        import aws_sdk_iot.types.billing_group_name_and_arn_list

        out["billing_groups"] = (
            aws_sdk_iot.types.billing_group_name_and_arn_list.deserialize_json(
                data["billingGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
