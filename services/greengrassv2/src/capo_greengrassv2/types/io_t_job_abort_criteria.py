"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IoTJobAbortCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_greengrassv2.types.io_t_job_abort_action
    import capo_greengrassv2.types.io_t_job_abort_threshold_percentage
    import capo_greengrassv2.types.io_t_job_execution_failure_type
    import capo_greengrassv2.types.io_t_job_minimum_number_of_executed_things


class IoTJobAbortCriteria(TypedDict, closed=True):
    failure_type: "capo_greengrassv2.types.io_t_job_execution_failure_type.IoTJobExecutionFailureType"
    """<p>The type of job deployment failure that can cancel a job.</p>"""
    action: "capo_greengrassv2.types.io_t_job_abort_action.IoTJobAbortAction"
    """<p>The action to perform when the criteria are met.</p>"""
    threshold_percentage: "capo_greengrassv2.types.io_t_job_abort_threshold_percentage.IoTJobAbortThresholdPercentage"
    """<p>The minimum percentage of <code>failureType</code> failures that occur before the job can cancel.</p> <p>This parameter supports up to two digits after the decimal (for example, you can specify <code>10.9</code> or <code>10.99</code>, but not <code>10.999</code>).</p>"""
    min_number_of_executed_things: "capo_greengrassv2.types.io_t_job_minimum_number_of_executed_things.IoTJobMinimumNumberOfExecutedThings"
    """<p>The minimum number of things that receive the configuration before the job can cancel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IoTJobAbortCriteria) -> dict:
    out: dict = {}
    import capo_greengrassv2.types.io_t_job_execution_failure_type

    out["failureType"] = (
        capo_greengrassv2.types.io_t_job_execution_failure_type.serialize_json(
            value["failure_type"]
        )
    )
    import capo_greengrassv2.types.io_t_job_abort_action

    out["action"] = capo_greengrassv2.types.io_t_job_abort_action.serialize_json(
        value["action"]
    )
    out["thresholdPercentage"] = value.get("threshold_percentage", 0)
    out["minNumberOfExecutedThings"] = value["min_number_of_executed_things"]
    return out


def deserialize_json(data: dict) -> IoTJobAbortCriteria:
    out: IoTJobAbortCriteria = {}  # type: ignore[typeddict-item]
    if "failureType" in data:
        import capo_greengrassv2.types.io_t_job_execution_failure_type

        out["failure_type"] = (
            capo_greengrassv2.types.io_t_job_execution_failure_type.deserialize_json(
                data["failureType"]
            )
        )
    else:
        raise DeserializationError("IoTJobAbortCriteria.failure_type required")
    if "action" in data:
        import capo_greengrassv2.types.io_t_job_abort_action

        out["action"] = capo_greengrassv2.types.io_t_job_abort_action.deserialize_json(
            data["action"]
        )
    else:
        raise DeserializationError("IoTJobAbortCriteria.action required")
    if "thresholdPercentage" in data:
        out["threshold_percentage"] = data["thresholdPercentage"]
    else:
        out["threshold_percentage"] = 0
    if "minNumberOfExecutedThings" in data:
        out["min_number_of_executed_things"] = data["minNumberOfExecutedThings"]
    else:
        raise DeserializationError(
            "IoTJobAbortCriteria.min_number_of_executed_things required"
        )
    return out
