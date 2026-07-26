"""Generated from Smithy shape ``com.amazonaws.iot#AbortCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.abort_action
    import capo_iot.types.abort_threshold_percentage
    import capo_iot.types.job_execution_failure_type
    import capo_iot.types.minimum_number_of_executed_things


class AbortCriteria(TypedDict, closed=True):
    failure_type: "capo_iot.types.job_execution_failure_type.JobExecutionFailureType"
    """<p>The type of job execution failures that can initiate a job abort.</p>"""
    action: "capo_iot.types.abort_action.AbortAction"
    """<p>The type of job action to take to initiate the job abort.</p>"""
    threshold_percentage: (
        "capo_iot.types.abort_threshold_percentage.AbortThresholdPercentage"
    )
    """<p>The minimum percentage of job execution failures that must occur to initiate the job abort.</p> <p>Amazon Web Services IoT Core supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).</p>"""
    min_number_of_executed_things: (
        "capo_iot.types.minimum_number_of_executed_things.MinimumNumberOfExecutedThings"
    )
    """<p>The minimum number of things which must receive job execution notifications before the job can be aborted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AbortCriteria) -> dict:
    out: dict = {}
    import capo_iot.types.job_execution_failure_type

    out["failureType"] = capo_iot.types.job_execution_failure_type.serialize_json(
        value["failure_type"]
    )
    import capo_iot.types.abort_action

    out["action"] = capo_iot.types.abort_action.serialize_json(value["action"])
    out["thresholdPercentage"] = value["threshold_percentage"]
    out["minNumberOfExecutedThings"] = value["min_number_of_executed_things"]
    return out


def deserialize_json(data: dict) -> AbortCriteria:
    out: AbortCriteria = {}  # type: ignore[typeddict-item]
    if "failureType" in data:
        import capo_iot.types.job_execution_failure_type

        out["failure_type"] = (
            capo_iot.types.job_execution_failure_type.deserialize_json(
                data["failureType"]
            )
        )
    else:
        raise DeserializationError("AbortCriteria.failure_type required")
    if "action" in data:
        import capo_iot.types.abort_action

        out["action"] = capo_iot.types.abort_action.deserialize_json(data["action"])
    else:
        raise DeserializationError("AbortCriteria.action required")
    if "thresholdPercentage" in data:
        out["threshold_percentage"] = data["thresholdPercentage"]
    else:
        raise DeserializationError("AbortCriteria.threshold_percentage required")
    if "minNumberOfExecutedThings" in data:
        out["min_number_of_executed_things"] = data["minNumberOfExecutedThings"]
    else:
        raise DeserializationError(
            "AbortCriteria.min_number_of_executed_things required"
        )
    return out
