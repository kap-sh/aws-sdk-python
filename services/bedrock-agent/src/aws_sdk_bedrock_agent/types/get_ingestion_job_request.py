"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetIngestionJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.id


class GetIngestionJobRequest(TypedDict):
    knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base for the data ingestion job you want to get information on.</p>"""
    data_source_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source for the data ingestion job you want to get information on.</p>"""
    ingestion_job_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data ingestion job you want to get information on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIngestionJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIngestionJobRequest:
    out: GetIngestionJobRequest = {}  # type: ignore[typeddict-item]
    return out
