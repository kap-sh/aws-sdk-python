"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListBillingGroupsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_list
    import aws_sdk_billingconductor.types.token


class ListBillingGroupsOutput(TypedDict):
    billing_groups: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_list.BillingGroupList"
    ]
    """<p>A list of <code>BillingGroupListElement</code> retrieved. </p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p>The pagination token that's used on subsequent calls to get billing groups. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBillingGroupsOutput) -> dict:
    out: dict = {}
    if "billing_groups" in value:
        import aws_sdk_billingconductor.types.billing_group_list

        out["BillingGroups"] = (
            aws_sdk_billingconductor.types.billing_group_list.serialize_json(
                value["billing_groups"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBillingGroupsOutput:
    out: ListBillingGroupsOutput = {}  # type: ignore[typeddict-item]
    if "BillingGroups" in data:
        import aws_sdk_billingconductor.types.billing_group_list

        out["billing_groups"] = (
            aws_sdk_billingconductor.types.billing_group_list.deserialize_json(
                data["BillingGroups"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
