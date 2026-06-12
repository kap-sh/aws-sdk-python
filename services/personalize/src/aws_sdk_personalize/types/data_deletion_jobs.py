"""Generated from Smithy shape ``com.amazonaws.personalize#DataDeletionJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.data_deletion_job_summary

DataDeletionJobs: TypeAlias = list[
    "aws_sdk_personalize.types.data_deletion_job_summary.DataDeletionJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataDeletionJobs) -> list:
    import aws_sdk_personalize.types.data_deletion_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize.types.data_deletion_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataDeletionJobs:
    import aws_sdk_personalize.types.data_deletion_job_summary

    out: DataDeletionJobs = []
    for item in data:
        out.append(
            aws_sdk_personalize.types.data_deletion_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
