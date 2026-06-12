"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListMetadataTransferJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.metadata_transfer_job_summaries
    import aws_sdk_iottwinmaker.types.next_token


class ListMetadataTransferJobsResponse(TypedDict):
    metadata_transfer_job_summaries: "aws_sdk_iottwinmaker.types.metadata_transfer_job_summaries.MetadataTransferJobSummaries"
    """<p>The metadata transfer job summaries.</p>"""
    next_token: NotRequired["aws_sdk_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMetadataTransferJobsResponse) -> dict:
    out: dict = {}
    import aws_sdk_iottwinmaker.types.metadata_transfer_job_summaries

    out["metadataTransferJobSummaries"] = (
        aws_sdk_iottwinmaker.types.metadata_transfer_job_summaries.serialize_json(
            value["metadata_transfer_job_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMetadataTransferJobsResponse:
    out: ListMetadataTransferJobsResponse = {}  # type: ignore[typeddict-item]
    if "metadataTransferJobSummaries" in data:
        import aws_sdk_iottwinmaker.types.metadata_transfer_job_summaries

        out["metadata_transfer_job_summaries"] = (
            aws_sdk_iottwinmaker.types.metadata_transfer_job_summaries.deserialize_json(
                data["metadataTransferJobSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListMetadataTransferJobsResponse.metadata_transfer_job_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
