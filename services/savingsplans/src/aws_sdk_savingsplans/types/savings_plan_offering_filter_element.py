"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanOfferingFilterElement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.filter_values_list
    import aws_sdk_savingsplans.types.savings_plan_offering_filter_attribute


class SavingsPlanOfferingFilterElement(TypedDict):
    name: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_offering_filter_attribute.SavingsPlanOfferingFilterAttribute"
    ]
    """<p>The filter name.</p>"""
    values: NotRequired[
        "aws_sdk_savingsplans.types.filter_values_list.FilterValuesList"
    ]
    """<p>The filter values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanOfferingFilterElement) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_savingsplans.types.savings_plan_offering_filter_attribute

        out["name"] = (
            aws_sdk_savingsplans.types.savings_plan_offering_filter_attribute.serialize_json(
                value["name"]
            )
        )
    if "values" in value:
        import aws_sdk_savingsplans.types.filter_values_list

        out["values"] = aws_sdk_savingsplans.types.filter_values_list.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> SavingsPlanOfferingFilterElement:
    out: SavingsPlanOfferingFilterElement = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_savingsplans.types.savings_plan_offering_filter_attribute

        out["name"] = (
            aws_sdk_savingsplans.types.savings_plan_offering_filter_attribute.deserialize_json(
                data["name"]
            )
        )
    if "values" in data:
        import aws_sdk_savingsplans.types.filter_values_list

        out["values"] = aws_sdk_savingsplans.types.filter_values_list.deserialize_json(
            data["values"]
        )
    return out
