"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DataSourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.data_source_status
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.name


class DataSourceSummary(TypedDict, closed=True):
    knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base to which the data source belongs.</p>"""
    data_source_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source.</p>"""
    name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The name of the data source.</p>"""
    status: "aws_sdk_bedrock_agent.types.data_source_status.DataSourceStatus"
    """<p>The status of the data source.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>The description of the data source.</p>"""
    updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the data source was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSummary) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["dataSourceId"] = value["data_source_id"]
    out["name"] = value["name"]
    import aws_sdk_bedrock_agent.types.data_source_status

    out["status"] = aws_sdk_bedrock_agent.types.data_source_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> DataSourceSummary:
    out: DataSourceSummary = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("DataSourceSummary.knowledge_base_id required")
    if "dataSourceId" in data:
        out["data_source_id"] = data["dataSourceId"]
    else:
        raise DeserializationError("DataSourceSummary.data_source_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DataSourceSummary.name required")
    if "status" in data:
        import aws_sdk_bedrock_agent.types.data_source_status

        out["status"] = aws_sdk_bedrock_agent.types.data_source_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DataSourceSummary.status required")
    if "description" in data:
        out["description"] = data["description"]
    if "updatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["updated_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("DataSourceSummary.updated_at required")
    return out
