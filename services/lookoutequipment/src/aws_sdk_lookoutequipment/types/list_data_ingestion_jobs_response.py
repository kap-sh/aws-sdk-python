"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListDataIngestionJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.data_ingestion_job_summaries
    import aws_sdk_lookoutequipment.types.next_token


class ListDataIngestionJobsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p> An opaque pagination token indicating where to continue the listing of data ingestion jobs. </p>"""
    data_ingestion_job_summaries: NotRequired[
        "aws_sdk_lookoutequipment.types.data_ingestion_job_summaries.DataIngestionJobSummaries"
    ]
    """<p>Specifies information about the specific data ingestion job, including dataset name and status. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDataIngestionJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "data_ingestion_job_summaries" in value:
        import aws_sdk_lookoutequipment.types.data_ingestion_job_summaries

        out["DataIngestionJobSummaries"] = (
            aws_sdk_lookoutequipment.types.data_ingestion_job_summaries.serialize_aws_json_1_0(
                value["data_ingestion_job_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDataIngestionJobsResponse:
    out: ListDataIngestionJobsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DataIngestionJobSummaries" in data:
        import aws_sdk_lookoutequipment.types.data_ingestion_job_summaries

        out["data_ingestion_job_summaries"] = (
            aws_sdk_lookoutequipment.types.data_ingestion_job_summaries.deserialize_aws_json_1_0(
                data["DataIngestionJobSummaries"]
            )
        )
    return out
