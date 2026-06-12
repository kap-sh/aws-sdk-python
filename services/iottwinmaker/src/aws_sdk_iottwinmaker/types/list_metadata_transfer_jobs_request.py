"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListMetadataTransferJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.destination_type
    import aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_filters
    import aws_sdk_iottwinmaker.types.max_results
    import aws_sdk_iottwinmaker.types.next_token
    import aws_sdk_iottwinmaker.types.source_type


class ListMetadataTransferJobsRequest(TypedDict):
    source_type: "aws_sdk_iottwinmaker.types.source_type.SourceType"
    """<p>The metadata transfer job's source type.</p>"""
    destination_type: "aws_sdk_iottwinmaker.types.destination_type.DestinationType"
    """<p>The metadata transfer job's destination type.</p>"""
    filters: NotRequired[
        "aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_filters.ListMetadataTransferJobsFilters"
    ]
    """<p>An object that filters metadata transfer jobs.</p>"""
    next_token: NotRequired["aws_sdk_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_iottwinmaker.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMetadataTransferJobsRequest) -> dict:
    out: dict = {}
    out["sourceType"] = value["source_type"]
    out["destinationType"] = value["destination_type"]
    if "filters" in value:
        import aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_filters

        out["filters"] = (
            aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_filters.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListMetadataTransferJobsRequest:
    out: ListMetadataTransferJobsRequest = {}  # type: ignore[typeddict-item]
    if "sourceType" in data:
        out["source_type"] = data["sourceType"]
    else:
        raise DeserializationError(
            "ListMetadataTransferJobsRequest.source_type required"
        )
    if "destinationType" in data:
        out["destination_type"] = data["destinationType"]
    else:
        raise DeserializationError(
            "ListMetadataTransferJobsRequest.destination_type required"
        )
    if "filters" in data:
        import aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_filters

        out["filters"] = (
            aws_sdk_iottwinmaker.types.list_metadata_transfer_jobs_filters.deserialize_json(
                data["filters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
