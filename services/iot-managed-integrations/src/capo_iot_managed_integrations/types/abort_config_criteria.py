"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AbortConfigCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.abort_criteria_action
    import capo_iot_managed_integrations.types.abort_criteria_failure_type
    import capo_iot_managed_integrations.types.min_number_of_executed_things
    import capo_iot_managed_integrations.types.threshold_percentage


class AbortConfigCriteria(TypedDict, closed=True):
    action: NotRequired[
        "capo_iot_managed_integrations.types.abort_criteria_action.AbortCriteriaAction"
    ]
    """<p>The action taken by the abort configuration.</p>"""
    failure_type: NotRequired[
        "capo_iot_managed_integrations.types.abort_criteria_failure_type.AbortCriteriaFailureType"
    ]
    """<p>Over-the-air (OTA) task abort criteria failure type.</p>"""
    min_number_of_executed_things: NotRequired[
        "capo_iot_managed_integrations.types.min_number_of_executed_things.MinNumberOfExecutedThings"
    ]
    """<p>The minimum number of things that must receive task execution notifications before the task can be aborted.</p>"""
    threshold_percentage: NotRequired[
        "capo_iot_managed_integrations.types.threshold_percentage.ThresholdPercentage"
    ]
    """<p>The minimum percentage of over-the-air (OTA) task execution failures that must occur to initiate the last abort.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AbortConfigCriteria) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_iot_managed_integrations.types.abort_criteria_action

        out["Action"] = (
            capo_iot_managed_integrations.types.abort_criteria_action.serialize_json(
                value["action"]
            )
        )
    if "failure_type" in value:
        import capo_iot_managed_integrations.types.abort_criteria_failure_type

        out["FailureType"] = (
            capo_iot_managed_integrations.types.abort_criteria_failure_type.serialize_json(
                value["failure_type"]
            )
        )
    if "min_number_of_executed_things" in value:
        out["MinNumberOfExecutedThings"] = value["min_number_of_executed_things"]
    if "threshold_percentage" in value:
        out["ThresholdPercentage"] = value["threshold_percentage"]
    return out


def deserialize_json(data: dict) -> AbortConfigCriteria:
    out: AbortConfigCriteria = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import capo_iot_managed_integrations.types.abort_criteria_action

        out["action"] = (
            capo_iot_managed_integrations.types.abort_criteria_action.deserialize_json(
                data["Action"]
            )
        )
    if "FailureType" in data:
        import capo_iot_managed_integrations.types.abort_criteria_failure_type

        out["failure_type"] = (
            capo_iot_managed_integrations.types.abort_criteria_failure_type.deserialize_json(
                data["FailureType"]
            )
        )
    if "MinNumberOfExecutedThings" in data:
        out["min_number_of_executed_things"] = data["MinNumberOfExecutedThings"]
    if "ThresholdPercentage" in data:
        out["threshold_percentage"] = data["ThresholdPercentage"]
    return out
