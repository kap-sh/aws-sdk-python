"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListMemoryExtractionJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.extraction_job_metadata_list
    import aws_sdk_bedrock_agentcore.types.pagination_token


class ListMemoryExtractionJobsOutput(TypedDict, closed=True):
    jobs: "aws_sdk_bedrock_agentcore.types.extraction_job_metadata_list.ExtractionJobMetadataList"
    """<p>List of extraction job metadata matching the specified criteria.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>Token to retrieve the next page of results, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMemoryExtractionJobsOutput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.extraction_job_metadata_list

    out["jobs"] = (
        aws_sdk_bedrock_agentcore.types.extraction_job_metadata_list.serialize_json(
            value["jobs"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMemoryExtractionJobsOutput:
    out: ListMemoryExtractionJobsOutput = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import aws_sdk_bedrock_agentcore.types.extraction_job_metadata_list

        out["jobs"] = (
            aws_sdk_bedrock_agentcore.types.extraction_job_metadata_list.deserialize_json(
                data["jobs"]
            )
        )
    else:
        raise DeserializationError("ListMemoryExtractionJobsOutput.jobs required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
