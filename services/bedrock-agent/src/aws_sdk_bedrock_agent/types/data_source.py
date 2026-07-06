"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.data_deletion_policy
    import aws_sdk_bedrock_agent.types.data_source_configuration
    import aws_sdk_bedrock_agent.types.data_source_status
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.failure_reasons
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.server_side_encryption_configuration
    import aws_sdk_bedrock_agent.types.vector_ingestion_configuration


class DataSource(TypedDict, closed=True):
    knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base to which the data source belongs.</p>"""
    data_source_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source.</p>"""
    name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The name of the data source.</p>"""
    status: "aws_sdk_bedrock_agent.types.data_source_status.DataSourceStatus"
    """<p>The status of the data source. The following statuses are possible:</p> <ul> <li> <p>Available – The data source has been created and is ready for ingestion into the knowledge base.</p> </li> <li> <p>Deleting – The data source is being deleted.</p> </li> </ul>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>The description of the data source.</p>"""
    data_source_configuration: (
        "aws_sdk_bedrock_agent.types.data_source_configuration.DataSourceConfiguration"
    )
    """<p>The connection configuration for the data source.</p>"""
    server_side_encryption_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>Contains details about the configuration of the server-side encryption.</p>"""
    vector_ingestion_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.vector_ingestion_configuration.VectorIngestionConfiguration"
    ]
    """<p>Contains details about how to ingest the documents in the data source.</p>"""
    data_deletion_policy: NotRequired[
        "aws_sdk_bedrock_agent.types.data_deletion_policy.DataDeletionPolicy"
    ]
    """<p>The data deletion policy for the data source.</p>"""
    created_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the data source was created.</p>"""
    updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the data source was last updated.</p>"""
    failure_reasons: NotRequired[
        "aws_sdk_bedrock_agent.types.failure_reasons.FailureReasons"
    ]
    """<p>The detailed reasons on the failure to delete a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSource) -> dict:
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
    import aws_sdk_bedrock_agent.types.data_source_configuration

    out["dataSourceConfiguration"] = (
        aws_sdk_bedrock_agent.types.data_source_configuration.serialize_json(
            value["data_source_configuration"]
        )
    )
    if "server_side_encryption_configuration" in value:
        import aws_sdk_bedrock_agent.types.server_side_encryption_configuration

        out["serverSideEncryptionConfiguration"] = (
            aws_sdk_bedrock_agent.types.server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    if "vector_ingestion_configuration" in value:
        import aws_sdk_bedrock_agent.types.vector_ingestion_configuration

        out["vectorIngestionConfiguration"] = (
            aws_sdk_bedrock_agent.types.vector_ingestion_configuration.serialize_json(
                value["vector_ingestion_configuration"]
            )
        )
    if "data_deletion_policy" in value:
        import aws_sdk_bedrock_agent.types.data_deletion_policy

        out["dataDeletionPolicy"] = (
            aws_sdk_bedrock_agent.types.data_deletion_policy.serialize_json(
                value["data_deletion_policy"]
            )
        )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "failure_reasons" in value:
        import aws_sdk_bedrock_agent.types.failure_reasons

        out["failureReasons"] = (
            aws_sdk_bedrock_agent.types.failure_reasons.serialize_json(
                value["failure_reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("DataSource.knowledge_base_id required")
    if "dataSourceId" in data:
        out["data_source_id"] = data["dataSourceId"]
    else:
        raise DeserializationError("DataSource.data_source_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DataSource.name required")
    if "status" in data:
        import aws_sdk_bedrock_agent.types.data_source_status

        out["status"] = aws_sdk_bedrock_agent.types.data_source_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DataSource.status required")
    if "description" in data:
        out["description"] = data["description"]
    if "dataSourceConfiguration" in data:
        import aws_sdk_bedrock_agent.types.data_source_configuration

        out["data_source_configuration"] = (
            aws_sdk_bedrock_agent.types.data_source_configuration.deserialize_json(
                data["dataSourceConfiguration"]
            )
        )
    else:
        raise DeserializationError("DataSource.data_source_configuration required")
    if "serverSideEncryptionConfiguration" in data:
        import aws_sdk_bedrock_agent.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            aws_sdk_bedrock_agent.types.server_side_encryption_configuration.deserialize_json(
                data["serverSideEncryptionConfiguration"]
            )
        )
    if "vectorIngestionConfiguration" in data:
        import aws_sdk_bedrock_agent.types.vector_ingestion_configuration

        out["vector_ingestion_configuration"] = (
            aws_sdk_bedrock_agent.types.vector_ingestion_configuration.deserialize_json(
                data["vectorIngestionConfiguration"]
            )
        )
    if "dataDeletionPolicy" in data:
        import aws_sdk_bedrock_agent.types.data_deletion_policy

        out["data_deletion_policy"] = (
            aws_sdk_bedrock_agent.types.data_deletion_policy.deserialize_json(
                data["dataDeletionPolicy"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["created_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("DataSource.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["updated_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("DataSource.updated_at required")
    if "failureReasons" in data:
        import aws_sdk_bedrock_agent.types.failure_reasons

        out["failure_reasons"] = (
            aws_sdk_bedrock_agent.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    return out
