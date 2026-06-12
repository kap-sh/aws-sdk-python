"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOffering``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.currency_code
    import aws_sdk_savingsplans.types.savings_plan_description
    import aws_sdk_savingsplans.types.savings_plan_offering_property_list
    import aws_sdk_savingsplans.types.savings_plan_operation
    import aws_sdk_savingsplans.types.savings_plan_payment_option
    import aws_sdk_savingsplans.types.savings_plan_product_type_list
    import aws_sdk_savingsplans.types.savings_plan_service_code
    import aws_sdk_savingsplans.types.savings_plan_type
    import aws_sdk_savingsplans.types.savings_plan_usage_type
    import aws_sdk_savingsplans.types.savings_plans_duration
    import aws_sdk_savingsplans.types.uuid


class SavingsPlanOffering(TypedDict):
    offering_id: NotRequired["aws_sdk_savingsplans.types.uuid.UUID"]
    """<p>The ID of the offering.</p>"""
    product_types: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_product_type_list.SavingsPlanProductTypeList"
    ]
    """<p>The product type.</p>"""
    plan_type: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_type.SavingsPlanType"
    ]
    """<p>The plan type.</p>"""
    description: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_description.SavingsPlanDescription"
    ]
    """<p>The description.</p>"""
    payment_option: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_payment_option.SavingsPlanPaymentOption"
    ]
    """<p>The payment option.</p>"""
    duration_seconds: (
        "aws_sdk_savingsplans.types.savings_plans_duration.SavingsPlansDuration"
    )
    """<p>The duration, in seconds.</p>"""
    currency: NotRequired["aws_sdk_savingsplans.types.currency_code.CurrencyCode"]
    """<p>The currency.</p>"""
    service_code: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_service_code.SavingsPlanServiceCode"
    ]
    """<p>The service.</p>"""
    usage_type: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_usage_type.SavingsPlanUsageType"
    ]
    """<p>The usage details of the line item in the billing report.</p>"""
    operation: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_operation.SavingsPlanOperation"
    ]
    """<p>The specific Amazon Web Services operation for the line item in the billing report.</p>"""
    properties: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_offering_property_list.SavingsPlanOfferingPropertyList"
    ]
    """<p>The properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOffering) -> dict:
    out: dict = {}
    if "offering_id" in value:
        out["offeringId"] = value["offering_id"]
    if "product_types" in value:
        import aws_sdk_savingsplans.types.savings_plan_product_type_list

        out["productTypes"] = (
            aws_sdk_savingsplans.types.savings_plan_product_type_list.serialize_json(
                value["product_types"]
            )
        )
    if "plan_type" in value:
        import aws_sdk_savingsplans.types.savings_plan_type

        out["planType"] = aws_sdk_savingsplans.types.savings_plan_type.serialize_json(
            value["plan_type"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "payment_option" in value:
        import aws_sdk_savingsplans.types.savings_plan_payment_option

        out["paymentOption"] = (
            aws_sdk_savingsplans.types.savings_plan_payment_option.serialize_json(
                value["payment_option"]
            )
        )
    out["durationSeconds"] = value.get("duration_seconds", 0)
    if "currency" in value:
        import aws_sdk_savingsplans.types.currency_code

        out["currency"] = aws_sdk_savingsplans.types.currency_code.serialize_json(
            value["currency"]
        )
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "usage_type" in value:
        out["usageType"] = value["usage_type"]
    if "operation" in value:
        out["operation"] = value["operation"]
    if "properties" in value:
        import aws_sdk_savingsplans.types.savings_plan_offering_property_list

        out["properties"] = (
            aws_sdk_savingsplans.types.savings_plan_offering_property_list.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> SavingsPlanOffering:
    out: SavingsPlanOffering = {}  # type: ignore[typeddict-item]
    if "offeringId" in data:
        out["offering_id"] = data["offeringId"]
    if "productTypes" in data:
        import aws_sdk_savingsplans.types.savings_plan_product_type_list

        out["product_types"] = (
            aws_sdk_savingsplans.types.savings_plan_product_type_list.deserialize_json(
                data["productTypes"]
            )
        )
    if "planType" in data:
        import aws_sdk_savingsplans.types.savings_plan_type

        out["plan_type"] = (
            aws_sdk_savingsplans.types.savings_plan_type.deserialize_json(
                data["planType"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "paymentOption" in data:
        import aws_sdk_savingsplans.types.savings_plan_payment_option

        out["payment_option"] = (
            aws_sdk_savingsplans.types.savings_plan_payment_option.deserialize_json(
                data["paymentOption"]
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
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    if "usageType" in data:
        out["usage_type"] = data["usageType"]
    if "operation" in data:
        out["operation"] = data["operation"]
    if "properties" in data:
        import aws_sdk_savingsplans.types.savings_plan_offering_property_list

        out["properties"] = (
            aws_sdk_savingsplans.types.savings_plan_offering_property_list.deserialize_json(
                data["properties"]
            )
        )
    return out
