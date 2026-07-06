"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListBillingGroupsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_arn_list
    import aws_sdk_billingconductor.types.billing_group_status_list
    import aws_sdk_billingconductor.types.billing_group_type_list
    import aws_sdk_billingconductor.types.pricing_plan_full_arn
    import aws_sdk_billingconductor.types.primary_account_id_list
    import aws_sdk_billingconductor.types.responsibility_transfer_arns_list
    import aws_sdk_billingconductor.types.string_searches


class ListBillingGroupsFilter(TypedDict, closed=True):
    arns: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_arn_list.BillingGroupArnList"
    ]
    """<p>The list of billing group Amazon Resource Names (ARNs) to retrieve information.</p>"""
    pricing_plan: NotRequired[
        "aws_sdk_billingconductor.types.pricing_plan_full_arn.PricingPlanFullArn"
    ]
    """<p>The pricing plan Amazon Resource Names (ARNs) to retrieve information.</p>"""
    statuses: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_status_list.BillingGroupStatusList"
    ]
    """<p> A list of billing groups to retrieve their current status for a specific time range </p>"""
    auto_associate: NotRequired["bool"]
    """<p>Specifies if this billing group will automatically associate newly added Amazon Web Services accounts that join your consolidated billing family.</p>"""
    primary_account_ids: NotRequired[
        "aws_sdk_billingconductor.types.primary_account_id_list.PrimaryAccountIdList"
    ]
    """<p> A list of primary account IDs to filter the billing groups. </p>"""
    billing_group_types: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_type_list.BillingGroupTypeList"
    ]
    """<p> Filter billing groups by their type. </p>"""
    names: NotRequired["aws_sdk_billingconductor.types.string_searches.StringSearches"]
    """<p> Filter billing groups by their names. </p>"""
    responsibility_transfer_arns: NotRequired[
        "aws_sdk_billingconductor.types.responsibility_transfer_arns_list.ResponsibilityTransferArnsList"
    ]
    """<p> Filter billing groups by their responsibility transfer ARNs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBillingGroupsFilter) -> dict:
    out: dict = {}
    if "arns" in value:
        import aws_sdk_billingconductor.types.billing_group_arn_list

        out["Arns"] = (
            aws_sdk_billingconductor.types.billing_group_arn_list.serialize_json(
                value["arns"]
            )
        )
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    if "statuses" in value:
        import aws_sdk_billingconductor.types.billing_group_status_list

        out["Statuses"] = (
            aws_sdk_billingconductor.types.billing_group_status_list.serialize_json(
                value["statuses"]
            )
        )
    if "auto_associate" in value:
        out["AutoAssociate"] = value["auto_associate"]
    if "primary_account_ids" in value:
        import aws_sdk_billingconductor.types.primary_account_id_list

        out["PrimaryAccountIds"] = (
            aws_sdk_billingconductor.types.primary_account_id_list.serialize_json(
                value["primary_account_ids"]
            )
        )
    if "billing_group_types" in value:
        import aws_sdk_billingconductor.types.billing_group_type_list

        out["BillingGroupTypes"] = (
            aws_sdk_billingconductor.types.billing_group_type_list.serialize_json(
                value["billing_group_types"]
            )
        )
    if "names" in value:
        import aws_sdk_billingconductor.types.string_searches

        out["Names"] = aws_sdk_billingconductor.types.string_searches.serialize_json(
            value["names"]
        )
    if "responsibility_transfer_arns" in value:
        import aws_sdk_billingconductor.types.responsibility_transfer_arns_list

        out["ResponsibilityTransferArns"] = (
            aws_sdk_billingconductor.types.responsibility_transfer_arns_list.serialize_json(
                value["responsibility_transfer_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListBillingGroupsFilter:
    out: ListBillingGroupsFilter = {}  # type: ignore[typeddict-item]
    if "Arns" in data:
        import aws_sdk_billingconductor.types.billing_group_arn_list

        out["arns"] = (
            aws_sdk_billingconductor.types.billing_group_arn_list.deserialize_json(
                data["Arns"]
            )
        )
    if "PricingPlan" in data:
        out["pricing_plan"] = data["PricingPlan"]
    if "Statuses" in data:
        import aws_sdk_billingconductor.types.billing_group_status_list

        out["statuses"] = (
            aws_sdk_billingconductor.types.billing_group_status_list.deserialize_json(
                data["Statuses"]
            )
        )
    if "AutoAssociate" in data:
        out["auto_associate"] = data["AutoAssociate"]
    if "PrimaryAccountIds" in data:
        import aws_sdk_billingconductor.types.primary_account_id_list

        out["primary_account_ids"] = (
            aws_sdk_billingconductor.types.primary_account_id_list.deserialize_json(
                data["PrimaryAccountIds"]
            )
        )
    if "BillingGroupTypes" in data:
        import aws_sdk_billingconductor.types.billing_group_type_list

        out["billing_group_types"] = (
            aws_sdk_billingconductor.types.billing_group_type_list.deserialize_json(
                data["BillingGroupTypes"]
            )
        )
    if "Names" in data:
        import aws_sdk_billingconductor.types.string_searches

        out["names"] = aws_sdk_billingconductor.types.string_searches.deserialize_json(
            data["Names"]
        )
    if "ResponsibilityTransferArns" in data:
        import aws_sdk_billingconductor.types.responsibility_transfer_arns_list

        out["responsibility_transfer_arns"] = (
            aws_sdk_billingconductor.types.responsibility_transfer_arns_list.deserialize_json(
                data["ResponsibilityTransferArns"]
            )
        )
    return out
