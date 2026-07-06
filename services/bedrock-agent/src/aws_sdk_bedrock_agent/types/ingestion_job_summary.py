"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.ingestion_job_statistics
    import aws_sdk_bedrock_agent.types.ingestion_job_status


class IngestionJobSummary(TypedDict, closed=True):
    knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base for the data ingestion job.</p>"""
    data_source_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source for the data ingestion job.</p>"""
    ingestion_job_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data ingestion job.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>The description of the data ingestion job.</p>"""
    status: "aws_sdk_bedrock_agent.types.ingestion_job_status.IngestionJobStatus"
    """<p>The status of the data ingestion job.</p>"""
    started_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time the data ingestion job started.</p>"""
    updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time the data ingestion job was last updated.</p>"""
    statistics: NotRequired[
        "aws_sdk_bedrock_agent.types.ingestion_job_statistics.IngestionJobStatistics"
    ]
    """<p>Contains statistics for the data ingestion job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJobSummary) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["dataSourceId"] = value["data_source_id"]
    out["ingestionJobId"] = value["ingestion_job_id"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agent.types.ingestion_job_status

    out["status"] = aws_sdk_bedrock_agent.types.ingestion_job_status.serialize_json(
        value["status"]
    )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["startedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["started_at"]
    )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "statistics" in value:
        import aws_sdk_bedrock_agent.types.ingestion_job_statistics

        out["statistics"] = (
            aws_sdk_bedrock_agent.types.ingestion_job_statistics.serialize_json(
                value["statistics"]
            )
        )
    return out


def deserialize_json(data: dict) -> IngestionJobSummary:
    out: IngestionJobSummary = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("IngestionJobSummary.knowledge_base_id required")
    if "dataSourceId" in data:
        out["data_source_id"] = data["dataSourceId"]
    else:
        raise DeserializationError("IngestionJobSummary.data_source_id required")
    if "ingestionJobId" in data:
        out["ingestion_job_id"] = data["ingestionJobId"]
    else:
        raise DeserializationError("IngestionJobSummary.ingestion_job_id required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_bedrock_agent.types.ingestion_job_status

        out["status"] = (
            aws_sdk_bedrock_agent.types.ingestion_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("IngestionJobSummary.status required")
    if "startedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["started_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["startedAt"]
        )
    else:
        raise DeserializationError("IngestionJobSummary.started_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["updated_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("IngestionJobSummary.updated_at required")
    if "statistics" in data:
        import aws_sdk_bedrock_agent.types.ingestion_job_statistics

        out["statistics"] = (
            aws_sdk_bedrock_agent.types.ingestion_job_statistics.deserialize_json(
                data["statistics"]
            )
        )
    return out
