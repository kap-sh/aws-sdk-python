"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateDataSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.data_deletion_policy
    import aws_sdk_bedrock_agent.types.data_source_configuration
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.server_side_encryption_configuration
    import aws_sdk_bedrock_agent.types.vector_ingestion_configuration


class UpdateDataSourceRequest(TypedDict):
    knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base for the data source.</p>"""
    data_source_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source.</p>"""
    name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>Specifies a new name for the data source.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>Specifies a new description for the data source.</p>"""
    data_source_configuration: (
        "aws_sdk_bedrock_agent.types.data_source_configuration.DataSourceConfiguration"
    )
    """<p>The connection configuration for the data source that you want to update.</p>"""
    data_deletion_policy: NotRequired[
        "aws_sdk_bedrock_agent.types.data_deletion_policy.DataDeletionPolicy"
    ]
    """<p>The data deletion policy for the data source that you want to update.</p>"""
    server_side_encryption_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>Contains details about server-side encryption of the data source.</p>"""
    vector_ingestion_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.vector_ingestion_configuration.VectorIngestionConfiguration"
    ]
    """<p>Contains details about how to ingest the documents in the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSourceRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agent.types.data_source_configuration

    out["dataSourceConfiguration"] = (
        aws_sdk_bedrock_agent.types.data_source_configuration.serialize_json(
            value["data_source_configuration"]
        )
    )
    if "data_deletion_policy" in value:
        import aws_sdk_bedrock_agent.types.data_deletion_policy

        out["dataDeletionPolicy"] = (
            aws_sdk_bedrock_agent.types.data_deletion_policy.serialize_json(
                value["data_deletion_policy"]
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
    return out


def deserialize_json(data: dict) -> UpdateDataSourceRequest:
    out: UpdateDataSourceRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateDataSourceRequest.name required")
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
        raise DeserializationError(
            "UpdateDataSourceRequest.data_source_configuration required"
        )
    if "dataDeletionPolicy" in data:
        import aws_sdk_bedrock_agent.types.data_deletion_policy

        out["data_deletion_policy"] = (
            aws_sdk_bedrock_agent.types.data_deletion_policy.deserialize_json(
                data["dataDeletionPolicy"]
            )
        )
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
    return out
