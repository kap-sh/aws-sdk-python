"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteDataSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.data_source_status
    import aws_sdk_bedrock_agent.types.id


class DeleteDataSourceResponse(TypedDict, closed=True):
    knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base to which the data source that was deleted belonged.</p>"""
    data_source_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source that was deleted.</p>"""
    status: "aws_sdk_bedrock_agent.types.data_source_status.DataSourceStatus"
    """<p>The status of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSourceResponse) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["dataSourceId"] = value["data_source_id"]
    import aws_sdk_bedrock_agent.types.data_source_status

    out["status"] = aws_sdk_bedrock_agent.types.data_source_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteDataSourceResponse:
    out: DeleteDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError(
            "DeleteDataSourceResponse.knowledge_base_id required"
        )
    if "dataSourceId" in data:
        out["data_source_id"] = data["dataSourceId"]
    else:
        raise DeserializationError("DeleteDataSourceResponse.data_source_id required")
    if "status" in data:
        import aws_sdk_bedrock_agent.types.data_source_status

        out["status"] = aws_sdk_bedrock_agent.types.data_source_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeleteDataSourceResponse.status required")
    return out
