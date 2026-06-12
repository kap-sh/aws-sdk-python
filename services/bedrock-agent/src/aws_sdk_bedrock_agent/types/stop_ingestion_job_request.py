"""Generated from Smithy shape ``com.amazonaws.bedrockagent#StopIngestionJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.id


class StopIngestionJobRequest(TypedDict):
    knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base for the data ingestion job you want to stop.</p>"""
    data_source_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source for the data ingestion job you want to stop.</p>"""
    ingestion_job_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data ingestion job you want to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopIngestionJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopIngestionJobRequest:
    out: StopIngestionJobRequest = {}  # type: ignore[typeddict-item]
    return out
