"""Generated from Smithy shape ``com.amazonaws.emrserverless#JobRunAttempts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.job_run_attempt_summary

JobRunAttempts: TypeAlias = list[
    "aws_sdk_emr_serverless.types.job_run_attempt_summary.JobRunAttemptSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobRunAttempts) -> list:
    import aws_sdk_emr_serverless.types.job_run_attempt_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_emr_serverless.types.job_run_attempt_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> JobRunAttempts:
    import aws_sdk_emr_serverless.types.job_run_attempt_summary

    out: JobRunAttempts = []
    for item in data:
        out.append(
            aws_sdk_emr_serverless.types.job_run_attempt_summary.deserialize_json(item)
        )
    return out
