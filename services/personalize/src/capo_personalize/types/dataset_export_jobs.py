"""Generated from Smithy shape ``com.amazonaws.personalize#DatasetExportJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.dataset_export_job_summary

DatasetExportJobs: TypeAlias = list[
    "capo_personalize.types.dataset_export_job_summary.DatasetExportJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetExportJobs) -> list:
    import capo_personalize.types.dataset_export_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_personalize.types.dataset_export_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DatasetExportJobs:
    import capo_personalize.types.dataset_export_job_summary

    out: DatasetExportJobs = []
    for item in data:
        out.append(
            capo_personalize.types.dataset_export_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
