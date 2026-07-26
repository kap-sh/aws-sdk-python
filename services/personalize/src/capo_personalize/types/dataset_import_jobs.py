"""Generated from Smithy shape ``com.amazonaws.personalize#DatasetImportJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.dataset_import_job_summary

DatasetImportJobs: TypeAlias = list[
    "capo_personalize.types.dataset_import_job_summary.DatasetImportJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetImportJobs) -> list:
    import capo_personalize.types.dataset_import_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_personalize.types.dataset_import_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DatasetImportJobs:
    import capo_personalize.types.dataset_import_job_summary

    out: DatasetImportJobs = []
    for item in data:
        out.append(
            capo_personalize.types.dataset_import_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
