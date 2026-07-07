"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanRateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.list_of_strings
    import aws_sdk_savingsplans.types.savings_plan_rate_filter_name


class SavingsPlanRateFilter(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_rate_filter_name.SavingsPlanRateFilterName"
    ]
    """<p>The filter name.</p>"""
    values: NotRequired["aws_sdk_savingsplans.types.list_of_strings.ListOfStrings"]
    """<p>The filter values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanRateFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_savingsplans.types.savings_plan_rate_filter_name

        out["name"] = (
            aws_sdk_savingsplans.types.savings_plan_rate_filter_name.serialize_json(
                value["name"]
            )
        )
    if "values" in value:
        import aws_sdk_savingsplans.types.list_of_strings

        out["values"] = aws_sdk_savingsplans.types.list_of_strings.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> SavingsPlanRateFilter:
    out: SavingsPlanRateFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_savingsplans.types.savings_plan_rate_filter_name

        out["name"] = (
            aws_sdk_savingsplans.types.savings_plan_rate_filter_name.deserialize_json(
                data["name"]
            )
        )
    if "values" in data:
        import aws_sdk_savingsplans.types.list_of_strings

        out["values"] = aws_sdk_savingsplans.types.list_of_strings.deserialize_json(
            data["values"]
        )
    return out
