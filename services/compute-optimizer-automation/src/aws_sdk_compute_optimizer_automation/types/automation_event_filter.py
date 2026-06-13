"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AutomationEventFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.automation_event_filter_name
    import aws_sdk_compute_optimizer_automation.types.filter_values


class AutomationEventFilter(TypedDict):
    name: "aws_sdk_compute_optimizer_automation.types.automation_event_filter_name.AutomationEventFilterName"
    """<p> The name of the filter to apply. </p>"""
    values: "aws_sdk_compute_optimizer_automation.types.filter_values.FilterValues"
    """<p> The values to use for the specified filter. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutomationEventFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_compute_optimizer_automation.types.filter_values

    out["values"] = (
        aws_sdk_compute_optimizer_automation.types.filter_values.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutomationEventFilter:
    out: AutomationEventFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AutomationEventFilter.name required")
    if "values" in data:
        import aws_sdk_compute_optimizer_automation.types.filter_values

        out["values"] = (
            aws_sdk_compute_optimizer_automation.types.filter_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    else:
        raise DeserializationError("AutomationEventFilter.values required")
    return out
