"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListDataIngestionJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.dataset_name
    import capo_lookoutequipment.types.ingestion_job_status
    import capo_lookoutequipment.types.max_results
    import capo_lookoutequipment.types.next_token


class ListDataIngestionJobsRequest(TypedDict, closed=True):
    dataset_name: NotRequired["capo_lookoutequipment.types.dataset_name.DatasetName"]
    """<p>The name of the dataset being used for the data ingestion job. </p>"""
    next_token: NotRequired["capo_lookoutequipment.types.next_token.NextToken"]
    """<p>An opaque pagination token indicating where to continue the listing of data ingestion jobs. </p>"""
    max_results: NotRequired["capo_lookoutequipment.types.max_results.MaxResults"]
    """<p> Specifies the maximum number of data ingestion jobs to list. </p>"""
    status: NotRequired[
        "capo_lookoutequipment.types.ingestion_job_status.IngestionJobStatus"
    ]
    """<p>Indicates the status of the data ingestion job. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDataIngestionJobsRequest) -> dict:
    out: dict = {}
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "status" in value:
        import capo_lookoutequipment.types.ingestion_job_status

        out["Status"] = (
            capo_lookoutequipment.types.ingestion_job_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDataIngestionJobsRequest:
    out: ListDataIngestionJobsRequest = {}  # type: ignore[typeddict-item]
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Status" in data:
        import capo_lookoutequipment.types.ingestion_job_status

        out["status"] = (
            capo_lookoutequipment.types.ingestion_job_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
