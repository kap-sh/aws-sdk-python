"""Generated from Smithy shape ``com.amazonaws.savingsplans#ParentSavingsPlanOffering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.currency_code
    import aws_sdk_savingsplans.types.savings_plan_description
    import aws_sdk_savingsplans.types.savings_plan_payment_option
    import aws_sdk_savingsplans.types.savings_plan_type
    import aws_sdk_savingsplans.types.savings_plans_duration
    import aws_sdk_savingsplans.types.uuid


class ParentSavingsPlanOffering(TypedDict, closed=True):
    offering_id: NotRequired["aws_sdk_savingsplans.types.uuid.UUID"]
    """<p>The ID of the offering.</p>"""
    payment_option: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_payment_option.SavingsPlanPaymentOption"
    ]
    """<p>The payment option.</p>"""
    plan_type: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_type.SavingsPlanType"
    ]
    """<p>The plan type.</p>"""
    duration_seconds: (
        "aws_sdk_savingsplans.types.savings_plans_duration.SavingsPlansDuration"
    )
    """<p>The duration, in seconds.</p>"""
    currency: NotRequired["aws_sdk_savingsplans.types.currency_code.CurrencyCode"]
    """<p>The currency.</p>"""
    plan_description: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_description.SavingsPlanDescription"
    ]
    """<p>The description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParentSavingsPlanOffering) -> dict:
    out: dict = {}
    if "offering_id" in value:
        out["offeringId"] = value["offering_id"]
    if "payment_option" in value:
        import aws_sdk_savingsplans.types.savings_plan_payment_option

        out["paymentOption"] = (
            aws_sdk_savingsplans.types.savings_plan_payment_option.serialize_json(
                value["payment_option"]
            )
        )
    if "plan_type" in value:
        import aws_sdk_savingsplans.types.savings_plan_type

        out["planType"] = aws_sdk_savingsplans.types.savings_plan_type.serialize_json(
            value["plan_type"]
        )
    out["durationSeconds"] = value.get("duration_seconds", 0)
    if "currency" in value:
        import aws_sdk_savingsplans.types.currency_code

        out["currency"] = aws_sdk_savingsplans.types.currency_code.serialize_json(
            value["currency"]
        )
    if "plan_description" in value:
        out["planDescription"] = value["plan_description"]
    return out


def deserialize_json(data: dict) -> ParentSavingsPlanOffering:
    out: ParentSavingsPlanOffering = {}  # type: ignore[typeddict-item]
    if "offeringId" in data:
        out["offering_id"] = data["offeringId"]
    if "paymentOption" in data:
        import aws_sdk_savingsplans.types.savings_plan_payment_option

        out["payment_option"] = (
            aws_sdk_savingsplans.types.savings_plan_payment_option.deserialize_json(
                data["paymentOption"]
            )
        )
    if "planType" in data:
        import aws_sdk_savingsplans.types.savings_plan_type

        out["plan_type"] = (
            aws_sdk_savingsplans.types.savings_plan_type.deserialize_json(
                data["planType"]
            )
        )
    if "durationSeconds" in data:
        out["duration_seconds"] = data["durationSeconds"]
    else:
        out["duration_seconds"] = 0
    if "currency" in data:
        import aws_sdk_savingsplans.types.currency_code

        out["currency"] = aws_sdk_savingsplans.types.currency_code.deserialize_json(
            data["currency"]
        )
    if "planDescription" in data:
        out["plan_description"] = data["planDescription"]
    return out
