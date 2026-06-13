"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateDatasetRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.data_source_type
    import aws_sdk_bedrock_agentcore_control.types.dataset_name
    import aws_sdk_bedrock_agentcore_control.types.dataset_schema_type
    import aws_sdk_bedrock_agentcore_control.types.kms_key_arn
    import aws_sdk_bedrock_agentcore_control.types.tags_map

class CreateDatasetRequest(TypedDict):
    client_token: NotRequired["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    dataset_name: "aws_sdk_bedrock_agentcore_control.types.dataset_name.DatasetName"
    """<p> Human-readable name for the dataset. Must be unique within the account. Immutable after creation. </p>"""
    description: NotRequired["str"]
    """<p> A description of the dataset. </p>"""
    source: "aws_sdk_bedrock_agentcore_control.types.data_source_type.DataSourceType"
    """<p> Source of initial examples. Provide either inline examples or an S3 URI pointing to a JSONL file. </p>"""
    schema_type: "aws_sdk_bedrock_agentcore_control.types.dataset_schema_type.DatasetSchemaType"
    """<p> Versioned schema type governing the structure of examples. Immutable after creation. </p>"""
    kms_key_arn: NotRequired["aws_sdk_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"]
    """<p> Optional KMS key ARN for server-side encryption on service Amazon S3 writes. </p>"""
    tags: NotRequired["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p> A map of tag keys and values to assign to the dataset. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["datasetName"] = value["dataset_name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.data_source_type
    out["source"] = aws_sdk_bedrock_agentcore_control.types.data_source_type.serialize_json(value["source"])
    import aws_sdk_bedrock_agentcore_control.types.dataset_schema_type
    out["schemaType"] = aws_sdk_bedrock_agentcore_control.types.dataset_schema_type.serialize_json(value["schema_type"])
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import aws_sdk_bedrock_agentcore_control.types.tags_map
        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "datasetName" in data:
        out["dataset_name"] = data["datasetName"]
    else:
        raise DeserializationError("CreateDatasetRequest.dataset_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "source" in data:
        import aws_sdk_bedrock_agentcore_control.types.data_source_type
        out["source"] = aws_sdk_bedrock_agentcore_control.types.data_source_type.deserialize_json(data["source"])
    else:
        raise DeserializationError("CreateDatasetRequest.source required")
    if "schemaType" in data:
        import aws_sdk_bedrock_agentcore_control.types.dataset_schema_type
        out["schema_type"] = aws_sdk_bedrock_agentcore_control.types.dataset_schema_type.deserialize_json(data["schemaType"])
    else:
        raise DeserializationError("CreateDatasetRequest.schema_type required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "tags" in data:
        import aws_sdk_bedrock_agentcore_control.types.tags_map
        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.deserialize_json(data["tags"])
    return out