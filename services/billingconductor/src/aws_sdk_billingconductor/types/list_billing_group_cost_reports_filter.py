"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListBillingGroupCostReportsFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_arn_list


class ListBillingGroupCostReportsFilter(TypedDict):
    billing_group_arns: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_arn_list.BillingGroupArnList"
    ]
    """<p>The list of Amazon Resource Names (ARNs) used to filter billing groups to retrieve reports. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBillingGroupCostReportsFilter) -> dict:
    out: dict = {}
    if "billing_group_arns" in value:
        import aws_sdk_billingconductor.types.billing_group_arn_list

        out["BillingGroupArns"] = (
            aws_sdk_billingconductor.types.billing_group_arn_list.serialize_json(
                value["billing_group_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListBillingGroupCostReportsFilter:
    out: ListBillingGroupCostReportsFilter = {}  # type: ignore[typeddict-item]
    if "BillingGroupArns" in data:
        import aws_sdk_billingconductor.types.billing_group_arn_list

        out["billing_group_arns"] = (
            aws_sdk_billingconductor.types.billing_group_arn_list.deserialize_json(
                data["BillingGroupArns"]
            )
        )
    return out
