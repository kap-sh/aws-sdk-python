"""Generated from Smithy shape ``com.amazonaws.personalize#DataDeletionJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.data_deletion_job_summary

DataDeletionJobs: TypeAlias = list[
    "capo_personalize.types.data_deletion_job_summary.DataDeletionJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataDeletionJobs) -> list:
    import capo_personalize.types.data_deletion_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_personalize.types.data_deletion_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataDeletionJobs:
    import capo_personalize.types.data_deletion_job_summary

    out: DataDeletionJobs = []
    for item in data:
        out.append(
            capo_personalize.types.data_deletion_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
