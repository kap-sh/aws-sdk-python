"""Generated from Smithy shape ``com.amazonaws.glue#BatchStopJobRunSuccessfulSubmissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.batch_stop_job_run_successful_submission

BatchStopJobRunSuccessfulSubmissionList: TypeAlias = list[
    "capo_glue.types.batch_stop_job_run_successful_submission.BatchStopJobRunSuccessfulSubmission"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchStopJobRunSuccessfulSubmissionList) -> list:
    import capo_glue.types.batch_stop_job_run_successful_submission

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.batch_stop_job_run_successful_submission.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchStopJobRunSuccessfulSubmissionList:
    import capo_glue.types.batch_stop_job_run_successful_submission

    out: BatchStopJobRunSuccessfulSubmissionList = []
    for item in data:
        out.append(
            capo_glue.types.batch_stop_job_run_successful_submission.deserialize_aws_json_1_1(
                item
            )
        )
    return out
