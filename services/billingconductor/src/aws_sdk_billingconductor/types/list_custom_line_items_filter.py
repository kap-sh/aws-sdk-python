"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemsFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.account_id_list
    import aws_sdk_billingconductor.types.billing_group_arn_list
    import aws_sdk_billingconductor.types.custom_line_item_arns
    import aws_sdk_billingconductor.types.custom_line_item_name_list


class ListCustomLineItemsFilter(TypedDict):
    names: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_name_list.CustomLineItemNameList"
    ]
    """<p>A list of custom line items to retrieve information.</p>"""
    billing_groups: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_arn_list.BillingGroupArnList"
    ]
    """<p>The billing group Amazon Resource Names (ARNs) to retrieve information.</p>"""
    arns: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_arns.CustomLineItemArns"
    ]
    """<p>A list of custom line item ARNs to retrieve information.</p>"""
    account_ids: NotRequired[
        "aws_sdk_billingconductor.types.account_id_list.AccountIdList"
    ]
    """<p>The Amazon Web Services accounts in which this custom line item will be applied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemsFilter) -> dict:
    out: dict = {}
    if "names" in value:
        import aws_sdk_billingconductor.types.custom_line_item_name_list

        out["Names"] = (
            aws_sdk_billingconductor.types.custom_line_item_name_list.serialize_json(
                value["names"]
            )
        )
    if "billing_groups" in value:
        import aws_sdk_billingconductor.types.billing_group_arn_list

        out["BillingGroups"] = (
            aws_sdk_billingconductor.types.billing_group_arn_list.serialize_json(
                value["billing_groups"]
            )
        )
    if "arns" in value:
        import aws_sdk_billingconductor.types.custom_line_item_arns

        out["Arns"] = (
            aws_sdk_billingconductor.types.custom_line_item_arns.serialize_json(
                value["arns"]
            )
        )
    if "account_ids" in value:
        import aws_sdk_billingconductor.types.account_id_list

        out["AccountIds"] = (
            aws_sdk_billingconductor.types.account_id_list.serialize_json(
                value["account_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCustomLineItemsFilter:
    out: ListCustomLineItemsFilter = {}  # type: ignore[typeddict-item]
    if "Names" in data:
        import aws_sdk_billingconductor.types.custom_line_item_name_list

        out["names"] = (
            aws_sdk_billingconductor.types.custom_line_item_name_list.deserialize_json(
                data["Names"]
            )
        )
    if "BillingGroups" in data:
        import aws_sdk_billingconductor.types.billing_group_arn_list

        out["billing_groups"] = (
            aws_sdk_billingconductor.types.billing_group_arn_list.deserialize_json(
                data["BillingGroups"]
            )
        )
    if "Arns" in data:
        import aws_sdk_billingconductor.types.custom_line_item_arns

        out["arns"] = (
            aws_sdk_billingconductor.types.custom_line_item_arns.deserialize_json(
                data["Arns"]
            )
        )
    if "AccountIds" in data:
        import aws_sdk_billingconductor.types.account_id_list

        out["account_ids"] = (
            aws_sdk_billingconductor.types.account_id_list.deserialize_json(
                data["AccountIds"]
            )
        )
    return out
