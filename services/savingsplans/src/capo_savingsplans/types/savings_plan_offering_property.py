"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_savingsplans.types.json_safe_filter_value_string
    import capo_savingsplans.types.savings_plan_offering_property_key


class SavingsPlanOfferingProperty(TypedDict, closed=True):
    name: NotRequired[
        "capo_savingsplans.types.savings_plan_offering_property_key.SavingsPlanOfferingPropertyKey"
    ]
    """<p>The property name.</p>"""
    value: NotRequired[
        "capo_savingsplans.types.json_safe_filter_value_string.JsonSafeFilterValueString"
    ]
    """<p>The property value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOfferingProperty) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_savingsplans.types.savings_plan_offering_property_key

        out["name"] = (
            capo_savingsplans.types.savings_plan_offering_property_key.serialize_json(
                value["name"]
            )
        )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SavingsPlanOfferingProperty:
    out: SavingsPlanOfferingProperty = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import capo_savingsplans.types.savings_plan_offering_property_key

        out["name"] = (
            capo_savingsplans.types.savings_plan_offering_property_key.deserialize_json(
                data["name"]
            )
        )
    if "value" in data:
        out["value"] = data["value"]
    return out
