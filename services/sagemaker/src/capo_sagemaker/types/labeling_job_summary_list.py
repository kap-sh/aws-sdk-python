"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelingJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.labeling_job_summary

LabelingJobSummaryList: TypeAlias = list[
    "capo_sagemaker.types.labeling_job_summary.LabelingJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelingJobSummaryList) -> list:
    import capo_sagemaker.types.labeling_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.labeling_job_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LabelingJobSummaryList:
    import capo_sagemaker.types.labeling_job_summary

    out: LabelingJobSummaryList = []
    for item in data:
        out.append(
            capo_sagemaker.types.labeling_job_summary.deserialize_aws_json_1_1(item)
        )
    return out
