"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.automation_rule_filter_name
    import capo_compute_optimizer_automation.types.filter_values


class Filter(TypedDict, closed=True):
    name: "capo_compute_optimizer_automation.types.automation_rule_filter_name.AutomationRuleFilterName"
    """<p>The name of the filter field to apply.</p>"""
    values: "capo_compute_optimizer_automation.types.filter_values.FilterValues"
    """<p>The list of values to filter by for the specified filter field.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Filter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_compute_optimizer_automation.types.filter_values

    out["values"] = (
        capo_compute_optimizer_automation.types.filter_values.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Filter.name required")
    if "values" in data:
        import capo_compute_optimizer_automation.types.filter_values

        out["values"] = (
            capo_compute_optimizer_automation.types.filter_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    else:
        raise DeserializationError("Filter.values required")
    return out
