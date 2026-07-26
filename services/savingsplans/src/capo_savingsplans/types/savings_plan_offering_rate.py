"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingRate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_savingsplans.types.parent_savings_plan_offering
    import capo_savingsplans.types.savings_plan_offering_rate_property_list
    import capo_savingsplans.types.savings_plan_product_type
    import capo_savingsplans.types.savings_plan_rate_operation
    import capo_savingsplans.types.savings_plan_rate_price_per_unit
    import capo_savingsplans.types.savings_plan_rate_service_code
    import capo_savingsplans.types.savings_plan_rate_unit
    import capo_savingsplans.types.savings_plan_rate_usage_type


class SavingsPlanOfferingRate(TypedDict, closed=True):
    savings_plan_offering: NotRequired[
        "capo_savingsplans.types.parent_savings_plan_offering.ParentSavingsPlanOffering"
    ]
    """<p>The Savings Plan offering.</p>"""
    rate: NotRequired[
        "capo_savingsplans.types.savings_plan_rate_price_per_unit.SavingsPlanRatePricePerUnit"
    ]
    """<p>The Savings Plan rate.</p>"""
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
        "capo_savingsplans.types.savings_plan_offering_rate_property_list.SavingsPlanOfferingRatePropertyList"
    ]
    """<p>The properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOfferingRate) -> dict:
    out: dict = {}
    if "savings_plan_offering" in value:
        import capo_savingsplans.types.parent_savings_plan_offering

        out["savingsPlanOffering"] = (
            capo_savingsplans.types.parent_savings_plan_offering.serialize_json(
                value["savings_plan_offering"]
            )
        )
    if "rate" in value:
        out["rate"] = value["rate"]
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
        import capo_savingsplans.types.savings_plan_offering_rate_property_list

        out["properties"] = (
            capo_savingsplans.types.savings_plan_offering_rate_property_list.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> SavingsPlanOfferingRate:
    out: SavingsPlanOfferingRate = {}  # type: ignore[typeddict-item]
    if "savingsPlanOffering" in data:
        import capo_savingsplans.types.parent_savings_plan_offering

        out["savings_plan_offering"] = (
            capo_savingsplans.types.parent_savings_plan_offering.deserialize_json(
                data["savingsPlanOffering"]
            )
        )
    if "rate" in data:
        out["rate"] = data["rate"]
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
        import capo_savingsplans.types.savings_plan_offering_rate_property_list

        out["properties"] = (
            capo_savingsplans.types.savings_plan_offering_rate_property_list.deserialize_json(
                data["properties"]
            )
        )
    return out
