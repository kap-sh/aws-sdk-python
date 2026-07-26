"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DataIngestionJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lookoutequipment.types.data_ingestion_job_summary

DataIngestionJobSummaries: TypeAlias = list[
    "capo_lookoutequipment.types.data_ingestion_job_summary.DataIngestionJobSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataIngestionJobSummaries) -> list:
    import capo_lookoutequipment.types.data_ingestion_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_lookoutequipment.types.data_ingestion_job_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DataIngestionJobSummaries:
    import capo_lookoutequipment.types.data_ingestion_job_summary

    out: DataIngestionJobSummaries = []
    for item in data:
        out.append(
            capo_lookoutequipment.types.data_ingestion_job_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
