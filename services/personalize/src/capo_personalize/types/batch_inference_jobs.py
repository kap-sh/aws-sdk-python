"""Generated from Smithy shape ``com.amazonaws.personalize#BatchInferenceJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.batch_inference_job_summary

BatchInferenceJobs: TypeAlias = list[
    "capo_personalize.types.batch_inference_job_summary.BatchInferenceJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchInferenceJobs) -> list:
    import capo_personalize.types.batch_inference_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_personalize.types.batch_inference_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchInferenceJobs:
    import capo_personalize.types.batch_inference_job_summary

    out: BatchInferenceJobs = []
    for item in data:
        out.append(
            capo_personalize.types.batch_inference_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
