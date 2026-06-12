"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlan``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.amount
    import aws_sdk_savingsplans.types.currency_code
    import aws_sdk_savingsplans.types.ec2_instance_family
    import aws_sdk_savingsplans.types.region
    import aws_sdk_savingsplans.types.savings_plan_arn
    import aws_sdk_savingsplans.types.savings_plan_id
    import aws_sdk_savingsplans.types.savings_plan_offering_id
    import aws_sdk_savingsplans.types.savings_plan_payment_option
    import aws_sdk_savingsplans.types.savings_plan_product_type_list
    import aws_sdk_savingsplans.types.savings_plan_state
    import aws_sdk_savingsplans.types.savings_plan_type
    import aws_sdk_savingsplans.types.string
    import aws_sdk_savingsplans.types.tag_map
    import aws_sdk_savingsplans.types.term_duration_in_seconds


class SavingsPlan(TypedDict):
    offering_id: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_offering_id.SavingsPlanOfferingId"
    ]
    """<p>The ID of the offering.</p>"""
    savings_plan_id: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_id.SavingsPlanId"
    ]
    """<p>The ID of the Savings Plan.</p>"""
    savings_plan_arn: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_arn.SavingsPlanArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Savings Plan.</p>"""
    description: NotRequired["aws_sdk_savingsplans.types.string.String"]
    """<p>The description.</p>"""
    start: NotRequired["aws_sdk_savingsplans.types.string.String"]
    """<p>The start time.</p>"""
    end: NotRequired["aws_sdk_savingsplans.types.string.String"]
    """<p>The end time.</p>"""
    state: NotRequired["aws_sdk_savingsplans.types.savings_plan_state.SavingsPlanState"]
    """<p>The current state.</p>"""
    region: NotRequired["aws_sdk_savingsplans.types.region.Region"]
    """<p>The Amazon Web Services Region.</p>"""
    ec2_instance_family: NotRequired[
        "aws_sdk_savingsplans.types.ec2_instance_family.EC2InstanceFamily"
    ]
    """<p>The EC2 instance family.</p>"""
    savings_plan_type: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_type.SavingsPlanType"
    ]
    """<p>The plan type.</p>"""
    payment_option: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_payment_option.SavingsPlanPaymentOption"
    ]
    """<p>The payment option.</p>"""
    product_types: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_product_type_list.SavingsPlanProductTypeList"
    ]
    """<p>The product types.</p>"""
    currency: NotRequired["aws_sdk_savingsplans.types.currency_code.CurrencyCode"]
    """<p>The currency.</p>"""
    commitment: NotRequired["aws_sdk_savingsplans.types.amount.Amount"]
    """<p>The hourly commitment amount in the specified currency.</p>"""
    upfront_payment_amount: NotRequired["aws_sdk_savingsplans.types.amount.Amount"]
    """<p>The up-front payment amount.</p>"""
    recurring_payment_amount: NotRequired["aws_sdk_savingsplans.types.amount.Amount"]
    """<p>The recurring payment amount.</p>"""
    term_duration_in_seconds: (
        "aws_sdk_savingsplans.types.term_duration_in_seconds.TermDurationInSeconds"
    )
    """<p>The duration of the term, in seconds.</p>"""
    tags: NotRequired["aws_sdk_savingsplans.types.tag_map.TagMap"]
    """<p>One or more tags.</p>"""
    returnable_until: NotRequired["aws_sdk_savingsplans.types.string.String"]
    """<p>The time until when a return for the Savings Plan can be requested. If the Savings Plan is not returnable, the field reflects the Savings Plans start time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlan) -> dict:
    out: dict = {}
    if "offering_id" in value:
        out["offeringId"] = value["offering_id"]
    if "savings_plan_id" in value:
        out["savingsPlanId"] = value["savings_plan_id"]
    if "savings_plan_arn" in value:
        out["savingsPlanArn"] = value["savings_plan_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "start" in value:
        out["start"] = value["start"]
    if "end" in value:
        out["end"] = value["end"]
    if "state" in value:
        import aws_sdk_savingsplans.types.savings_plan_state

        out["state"] = aws_sdk_savingsplans.types.savings_plan_state.serialize_json(
            value["state"]
        )
    if "region" in value:
        out["region"] = value["region"]
    if "ec2_instance_family" in value:
        out["ec2InstanceFamily"] = value["ec2_instance_family"]
    if "savings_plan_type" in value:
        import aws_sdk_savingsplans.types.savings_plan_type

        out["savingsPlanType"] = (
            aws_sdk_savingsplans.types.savings_plan_type.serialize_json(
                value["savings_plan_type"]
            )
        )
    if "payment_option" in value:
        import aws_sdk_savingsplans.types.savings_plan_payment_option

        out["paymentOption"] = (
            aws_sdk_savingsplans.types.savings_plan_payment_option.serialize_json(
                value["payment_option"]
            )
        )
    if "product_types" in value:
        import aws_sdk_savingsplans.types.savings_plan_product_type_list

        out["productTypes"] = (
            aws_sdk_savingsplans.types.savings_plan_product_type_list.serialize_json(
                value["product_types"]
            )
        )
    if "currency" in value:
        import aws_sdk_savingsplans.types.currency_code

        out["currency"] = aws_sdk_savingsplans.types.currency_code.serialize_json(
            value["currency"]
        )
    if "commitment" in value:
        out["commitment"] = value["commitment"]
    if "upfront_payment_amount" in value:
        out["upfrontPaymentAmount"] = value["upfront_payment_amount"]
    if "recurring_payment_amount" in value:
        out["recurringPaymentAmount"] = value["recurring_payment_amount"]
    out["termDurationInSeconds"] = value.get("term_duration_in_seconds", 0)
    if "tags" in value:
        import aws_sdk_savingsplans.types.tag_map

        out["tags"] = aws_sdk_savingsplans.types.tag_map.serialize_json(value["tags"])
    if "returnable_until" in value:
        out["returnableUntil"] = value["returnable_until"]
    return out


def deserialize_json(data: dict) -> SavingsPlan:
    out: SavingsPlan = {}  # type: ignore[typeddict-item]
    if "offeringId" in data:
        out["offering_id"] = data["offeringId"]
    if "savingsPlanId" in data:
        out["savings_plan_id"] = data["savingsPlanId"]
    if "savingsPlanArn" in data:
        out["savings_plan_arn"] = data["savingsPlanArn"]
    if "description" in data:
        out["description"] = data["description"]
    if "start" in data:
        out["start"] = data["start"]
    if "end" in data:
        out["end"] = data["end"]
    if "state" in data:
        import aws_sdk_savingsplans.types.savings_plan_state

        out["state"] = aws_sdk_savingsplans.types.savings_plan_state.deserialize_json(
            data["state"]
        )
    if "region" in data:
        out["region"] = data["region"]
    if "ec2InstanceFamily" in data:
        out["ec2_instance_family"] = data["ec2InstanceFamily"]
    if "savingsPlanType" in data:
        import aws_sdk_savingsplans.types.savings_plan_type

        out["savings_plan_type"] = (
            aws_sdk_savingsplans.types.savings_plan_type.deserialize_json(
                data["savingsPlanType"]
            )
        )
    if "paymentOption" in data:
        import aws_sdk_savingsplans.types.savings_plan_payment_option

        out["payment_option"] = (
            aws_sdk_savingsplans.types.savings_plan_payment_option.deserialize_json(
                data["paymentOption"]
            )
        )
    if "productTypes" in data:
        import aws_sdk_savingsplans.types.savings_plan_product_type_list

        out["product_types"] = (
            aws_sdk_savingsplans.types.savings_plan_product_type_list.deserialize_json(
                data["productTypes"]
            )
        )
    if "currency" in data:
        import aws_sdk_savingsplans.types.currency_code

        out["currency"] = aws_sdk_savingsplans.types.currency_code.deserialize_json(
            data["currency"]
        )
    if "commitment" in data:
        out["commitment"] = data["commitment"]
    if "upfrontPaymentAmount" in data:
        out["upfront_payment_amount"] = data["upfrontPaymentAmount"]
    if "recurringPaymentAmount" in data:
        out["recurring_payment_amount"] = data["recurringPaymentAmount"]
    if "termDurationInSeconds" in data:
        out["term_duration_in_seconds"] = data["termDurationInSeconds"]
    else:
        out["term_duration_in_seconds"] = 0
    if "tags" in data:
        import aws_sdk_savingsplans.types.tag_map

        out["tags"] = aws_sdk_savingsplans.types.tag_map.deserialize_json(data["tags"])
    if "returnableUntil" in data:
        out["returnable_until"] = data["returnableUntil"]
    return out
