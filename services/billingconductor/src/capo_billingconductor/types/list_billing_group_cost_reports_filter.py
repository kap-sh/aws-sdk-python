"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListBillingGroupCostReportsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_group_arn_list


class ListBillingGroupCostReportsFilter(TypedDict, closed=True):
    billing_group_arns: NotRequired[
        "capo_billingconductor.types.billing_group_arn_list.BillingGroupArnList"
    ]
    """<p>The list of Amazon Resource Names (ARNs) used to filter billing groups to retrieve reports. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBillingGroupCostReportsFilter) -> dict:
    out: dict = {}
    if "billing_group_arns" in value:
        import capo_billingconductor.types.billing_group_arn_list

        out["BillingGroupArns"] = (
            capo_billingconductor.types.billing_group_arn_list.serialize_json(
                value["billing_group_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListBillingGroupCostReportsFilter:
    out: ListBillingGroupCostReportsFilter = {}  # type: ignore[typeddict-item]
    if "BillingGroupArns" in data:
        import capo_billingconductor.types.billing_group_arn_list

        out["billing_group_arns"] = (
            capo_billingconductor.types.billing_group_arn_list.deserialize_json(
                data["BillingGroupArns"]
            )
        )
    return out
