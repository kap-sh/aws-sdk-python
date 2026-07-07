"""Generated from Smithy shape ``com.amazonaws.glue#BatchStopJobRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_stop_job_run_error_list
    import aws_sdk_glue.types.batch_stop_job_run_successful_submission_list


class BatchStopJobRunResponse(TypedDict, closed=True):
    successful_submissions: NotRequired[
        "aws_sdk_glue.types.batch_stop_job_run_successful_submission_list.BatchStopJobRunSuccessfulSubmissionList"
    ]
    """<p>A list of the JobRuns that were successfully submitted for stopping.</p>"""
    errors: NotRequired[
        "aws_sdk_glue.types.batch_stop_job_run_error_list.BatchStopJobRunErrorList"
    ]
    """<p>A list of the errors that were encountered in trying to stop <code>JobRuns</code>, including the <code>JobRunId</code> for which each error was encountered and details about the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchStopJobRunResponse) -> dict:
    out: dict = {}
    if "successful_submissions" in value:
        import aws_sdk_glue.types.batch_stop_job_run_successful_submission_list

        out["SuccessfulSubmissions"] = (
            aws_sdk_glue.types.batch_stop_job_run_successful_submission_list.serialize_aws_json_1_1(
                value["successful_submissions"]
            )
        )
    if "errors" in value:
        import aws_sdk_glue.types.batch_stop_job_run_error_list

        out["Errors"] = (
            aws_sdk_glue.types.batch_stop_job_run_error_list.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchStopJobRunResponse:
    out: BatchStopJobRunResponse = {}  # type: ignore[typeddict-item]
    if "SuccessfulSubmissions" in data:
        import aws_sdk_glue.types.batch_stop_job_run_successful_submission_list

        out["successful_submissions"] = (
            aws_sdk_glue.types.batch_stop_job_run_successful_submission_list.deserialize_aws_json_1_1(
                data["SuccessfulSubmissions"]
            )
        )
    if "Errors" in data:
        import aws_sdk_glue.types.batch_stop_job_run_error_list

        out["errors"] = (
            aws_sdk_glue.types.batch_stop_job_run_error_list.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    return out
