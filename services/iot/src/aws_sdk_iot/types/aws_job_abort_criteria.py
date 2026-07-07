"""Generated from Smithy shape ``com.amazonaws.iot#AwsJobAbortCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_job_abort_criteria_abort_action
    import aws_sdk_iot.types.aws_job_abort_criteria_abort_threshold_percentage
    import aws_sdk_iot.types.aws_job_abort_criteria_failure_type
    import aws_sdk_iot.types.aws_job_abort_criteria_minimum_number_of_executed_things


class AwsJobAbortCriteria(TypedDict, closed=True):
    failure_type: "aws_sdk_iot.types.aws_job_abort_criteria_failure_type.AwsJobAbortCriteriaFailureType"
    """<p>The type of job execution failures that can initiate a job abort.</p>"""
    action: "aws_sdk_iot.types.aws_job_abort_criteria_abort_action.AwsJobAbortCriteriaAbortAction"
    """<p>The type of job action to take to initiate the job abort.</p>"""
    threshold_percentage: "aws_sdk_iot.types.aws_job_abort_criteria_abort_threshold_percentage.AwsJobAbortCriteriaAbortThresholdPercentage"
    """<p>The minimum percentage of job execution failures that must occur to initiate the job abort.</p> <p>Amazon Web Services IoT Core supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).</p>"""
    min_number_of_executed_things: "aws_sdk_iot.types.aws_job_abort_criteria_minimum_number_of_executed_things.AwsJobAbortCriteriaMinimumNumberOfExecutedThings"
    """<p>The minimum number of things which must receive job execution notifications before the job can be aborted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsJobAbortCriteria) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.aws_job_abort_criteria_failure_type

    out["failureType"] = (
        aws_sdk_iot.types.aws_job_abort_criteria_failure_type.serialize_json(
            value["failure_type"]
        )
    )
    import aws_sdk_iot.types.aws_job_abort_criteria_abort_action

    out["action"] = (
        aws_sdk_iot.types.aws_job_abort_criteria_abort_action.serialize_json(
            value["action"]
        )
    )
    out["thresholdPercentage"] = value["threshold_percentage"]
    out["minNumberOfExecutedThings"] = value["min_number_of_executed_things"]
    return out


def deserialize_json(data: dict) -> AwsJobAbortCriteria:
    out: AwsJobAbortCriteria = {}  # type: ignore[typeddict-item]
    if "failureType" in data:
        import aws_sdk_iot.types.aws_job_abort_criteria_failure_type

        out["failure_type"] = (
            aws_sdk_iot.types.aws_job_abort_criteria_failure_type.deserialize_json(
                data["failureType"]
            )
        )
    else:
        raise DeserializationError("AwsJobAbortCriteria.failure_type required")
    if "action" in data:
        import aws_sdk_iot.types.aws_job_abort_criteria_abort_action

        out["action"] = (
            aws_sdk_iot.types.aws_job_abort_criteria_abort_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("AwsJobAbortCriteria.action required")
    if "thresholdPercentage" in data:
        out["threshold_percentage"] = data["thresholdPercentage"]
    else:
        raise DeserializationError("AwsJobAbortCriteria.threshold_percentage required")
    if "minNumberOfExecutedThings" in data:
        out["min_number_of_executed_things"] = data["minNumberOfExecutedThings"]
    else:
        raise DeserializationError(
            "AwsJobAbortCriteria.min_number_of_executed_things required"
        )
    return out
