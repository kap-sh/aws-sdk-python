"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_savingsplans.types.list_of_strings
    import capo_savingsplans.types.savings_plans_filter_name


class SavingsPlanFilter(TypedDict, closed=True):
    name: NotRequired[
        "capo_savingsplans.types.savings_plans_filter_name.SavingsPlansFilterName"
    ]
    """<p>The filter name.</p>"""
    values: NotRequired["capo_savingsplans.types.list_of_strings.ListOfStrings"]
    """<p>The filter value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_savingsplans.types.savings_plans_filter_name

        out["name"] = capo_savingsplans.types.savings_plans_filter_name.serialize_json(
            value["name"]
        )
    if "values" in value:
        import capo_savingsplans.types.list_of_strings

        out["values"] = capo_savingsplans.types.list_of_strings.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> SavingsPlanFilter:
    out: SavingsPlanFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import capo_savingsplans.types.savings_plans_filter_name

        out["name"] = (
            capo_savingsplans.types.savings_plans_filter_name.deserialize_json(
                data["name"]
            )
        )
    if "values" in data:
        import capo_savingsplans.types.list_of_strings

        out["values"] = capo_savingsplans.types.list_of_strings.deserialize_json(
            data["values"]
        )
    return out
