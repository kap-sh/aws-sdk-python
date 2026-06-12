"""Generated from Smithy shape ``com.amazonaws.forecast#DatasetImportJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.dataset_import_job_summary

DatasetImportJobs: TypeAlias = list[
    "aws_sdk_forecast.types.dataset_import_job_summary.DatasetImportJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetImportJobs) -> list:
    import aws_sdk_forecast.types.dataset_import_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.dataset_import_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DatasetImportJobs:
    import aws_sdk_forecast.types.dataset_import_job_summary

    out: DatasetImportJobs = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.dataset_import_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
