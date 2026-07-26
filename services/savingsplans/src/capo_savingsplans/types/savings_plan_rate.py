"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_savingsplans.types.amount
    import capo_savingsplans.types.currency_code
    import capo_savingsplans.types.savings_plan_product_type
    import capo_savingsplans.types.savings_plan_rate_operation
    import capo_savingsplans.types.savings_plan_rate_property_list
    import capo_savingsplans.types.savings_plan_rate_service_code
    import capo_savingsplans.types.savings_plan_rate_unit
    import capo_savingsplans.types.savings_plan_rate_usage_type


class SavingsPlanRate(TypedDict, closed=True):
    rate: NotRequired["capo_savingsplans.types.amount.Amount"]
    """<p>The rate.</p>"""
    currency: NotRequired["capo_savingsplans.types.currency_code.CurrencyCode"]
    """<p>The currency.</p>"""
    unit: NotRequired[
        "capo_savingsplans.types.savings_plan_rate_unit.SavingsPlanRateUnit"
    ]
    """<p>The unit.</p>"""
    product_type: NotRequired[
        "capo_savingsplans.types.savings_plan_product_type.SavingsPlanProductType"
    ]
    """<p>The product type.</p>"""
    service_code: NotRequired[
        "capo_savingsplans.types.savings_plan_rate_service_code.SavingsPlanRateServiceCode"
    ]
    """<p>The service.</p>"""
    usage_type: NotRequired[
        "capo_savingsplans.types.savings_plan_rate_usage_type.SavingsPlanRateUsageType"
    ]
    """<p>The usage details of the line item in the billing report.</p>"""
    operation: NotRequired[
        "capo_savingsplans.types.savings_plan_rate_operation.SavingsPlanRateOperation"
    ]
    """<p>The specific Amazon Web Services operation for the line item in the billing report.</p>"""
    properties: NotRequired[
        "capo_savingsplans.types.savings_plan_rate_property_list.SavingsPlanRatePropertyList"
    ]
    """<p>The properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanRate) -> dict:
    out: dict = {}
    if "rate" in value:
        out["rate"] = value["rate"]
    if "currency" in value:
        import capo_savingsplans.types.currency_code

        out["currency"] = capo_savingsplans.types.currency_code.serialize_json(
            value["currency"]
        )
    if "unit" in value:
        import capo_savingsplans.types.savings_plan_rate_unit

        out["unit"] = capo_savingsplans.types.savings_plan_rate_unit.serialize_json(
            value["unit"]
        )
    if "product_type" in value:
        import capo_savingsplans.types.savings_plan_product_type

        out["productType"] = (
            capo_savingsplans.types.savings_plan_product_type.serialize_json(
                value["product_type"]
            )
        )
    if "service_code" in value:
        import capo_savingsplans.types.savings_plan_rate_service_code

        out["serviceCode"] = (
            capo_savingsplans.types.savings_plan_rate_service_code.serialize_json(
                value["service_code"]
            )
        )
    if "usage_type" in value:
        out["usageType"] = value["usage_type"]
    if "operation" in value:
        out["operation"] = value["operation"]
    if "properties" in value:
        import capo_savingsplans.types.savings_plan_rate_property_list

        out["properties"] = (
            capo_savingsplans.types.savings_plan_rate_property_list.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> SavingsPlanRate:
    out: SavingsPlanRate = {}  # type: ignore[typeddict-item]
    if "rate" in data:
        out["rate"] = data["rate"]
    if "currency" in data:
        import capo_savingsplans.types.currency_code

        out["currency"] = capo_savingsplans.types.currency_code.deserialize_json(
            data["currency"]
        )
    if "unit" in data:
        import capo_savingsplans.types.savings_plan_rate_unit

        out["unit"] = capo_savingsplans.types.savings_plan_rate_unit.deserialize_json(
            data["unit"]
        )
    if "productType" in data:
        import capo_savingsplans.types.savings_plan_product_type

        out["product_type"] = (
            capo_savingsplans.types.savings_plan_product_type.deserialize_json(
                data["productType"]
            )
        )
    if "serviceCode" in data:
        import capo_savingsplans.types.savings_plan_rate_service_code

        out["service_code"] = (
            capo_savingsplans.types.savings_plan_rate_service_code.deserialize_json(
                data["serviceCode"]
            )
        )
    if "usageType" in data:
        out["usage_type"] = data["usageType"]
    if "operation" in data:
        out["operation"] = data["operation"]
    if "properties" in data:
        import capo_savingsplans.types.savings_plan_rate_property_list

        out["properties"] = (
            capo_savingsplans.types.savings_plan_rate_property_list.deserialize_json(
                data["properties"]
            )
        )
    return out
