"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetDatasetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore_control.types.dataset_arn
    import aws_sdk_bedrock_agentcore_control.types.dataset_id
    import aws_sdk_bedrock_agentcore_control.types.dataset_name
    import aws_sdk_bedrock_agentcore_control.types.dataset_schema_type
    import aws_sdk_bedrock_agentcore_control.types.dataset_status
    import aws_sdk_bedrock_agentcore_control.types.dataset_version
    import aws_sdk_bedrock_agentcore_control.types.download_url
    import aws_sdk_bedrock_agentcore_control.types.draft_status
    import aws_sdk_bedrock_agentcore_control.types.kms_key_arn
    import aws_sdk_bedrock_agentcore_control.types.tags_map


class GetDatasetResponse(TypedDict):
    dataset_arn: "aws_sdk_bedrock_agentcore_control.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset. </p>"""
    dataset_id: "aws_sdk_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    dataset_version: (
        "aws_sdk_bedrock_agentcore_control.types.dataset_version.DatasetVersion"
    )
    r"""<p> The resolved version: \"DRAFT\" (default) or the requested version number. </p>"""
    dataset_name: "aws_sdk_bedrock_agentcore_control.types.dataset_name.DatasetName"
    """<p> The name of the dataset. </p>"""
    description: NotRequired["str"]
    """<p> The description of the dataset. </p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.dataset_status.DatasetStatus"
    """<p> The current status of the dataset. </p>"""
    draft_status: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.draft_status.DraftStatus"
    ]
    """<p> Publish synchronization state. Only authoritative when status is ACTIVE. MODIFIED indicates DRAFT has unpublished changes. UNMODIFIED indicates DRAFT matches the latest published version. </p>"""
    failure_reason: NotRequired["str"]
    """<p> Populated when status is CREATE_FAILED, UPDATE_FAILED, or DELETE_FAILED. Describes the reason for the failure. </p>"""
    schema_type: (
        "aws_sdk_bedrock_agentcore_control.types.dataset_schema_type.DatasetSchemaType"
    )
    """<p> The schema type declared at create time. Immutable after creation. </p>"""
    kms_key_arn: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p> KMS key ARN used for server-side encryption on service Amazon S3 writes, if configured. </p>"""
    example_count: "int"
    """<p> The number of examples in the DRAFT. </p>"""
    download_url: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.download_url.DownloadUrl"
    ]
    """<p> Presigned Amazon S3 URL to download the consolidated dataset file for the resolved version. Expires after 5 minutes. Omitted if the file does not yet exist. </p>"""
    download_url_expires_at: NotRequired["datetime.datetime"]
    """<p> Expiry timestamp for the download URL. </p>"""
    created_at: "datetime.datetime"
    """<p> The timestamp when the dataset was created. </p>"""
    updated_at: "datetime.datetime"
    """<p> The timestamp when the dataset was last updated. </p>"""
    tags: NotRequired["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p> The tags associated with the dataset. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDatasetResponse) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    out["datasetId"] = value["dataset_id"]
    out["datasetVersion"] = value["dataset_version"]
    out["datasetName"] = value["dataset_name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.dataset_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.dataset_status.serialize_json(
            value["status"]
        )
    )
    if "draft_status" in value:
        import aws_sdk_bedrock_agentcore_control.types.draft_status

        out["draftStatus"] = (
            aws_sdk_bedrock_agentcore_control.types.draft_status.serialize_json(
                value["draft_status"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    import aws_sdk_bedrock_agentcore_control.types.dataset_schema_type

    out["schemaType"] = (
        aws_sdk_bedrock_agentcore_control.types.dataset_schema_type.serialize_json(
            value["schema_type"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    out["exampleCount"] = value["example_count"]
    if "download_url" in value:
        out["downloadUrl"] = value["download_url"]
    if "download_url_expires_at" in value:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["downloadUrlExpiresAt"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
                value["download_url_expires_at"]
            )
        )
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    if "tags" in value:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetDatasetResponse:
    out: GetDatasetResponse = {}  # type: ignore[typeddict-item]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("GetDatasetResponse.dataset_arn required")
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    else:
        raise DeserializationError("GetDatasetResponse.dataset_id required")
    if "datasetVersion" in data:
        out["dataset_version"] = data["datasetVersion"]
    else:
        raise DeserializationError("GetDatasetResponse.dataset_version required")
    if "datasetName" in data:
        out["dataset_name"] = data["datasetName"]
    else:
        raise DeserializationError("GetDatasetResponse.dataset_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.dataset_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.dataset_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetDatasetResponse.status required")
    if "draftStatus" in data:
        import aws_sdk_bedrock_agentcore_control.types.draft_status

        out["draft_status"] = (
            aws_sdk_bedrock_agentcore_control.types.draft_status.deserialize_json(
                data["draftStatus"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "schemaType" in data:
        import aws_sdk_bedrock_agentcore_control.types.dataset_schema_type

        out["schema_type"] = (
            aws_sdk_bedrock_agentcore_control.types.dataset_schema_type.deserialize_json(
                data["schemaType"]
            )
        )
    else:
        raise DeserializationError("GetDatasetResponse.schema_type required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "exampleCount" in data:
        out["example_count"] = data["exampleCount"]
    else:
        raise DeserializationError("GetDatasetResponse.example_count required")
    if "downloadUrl" in data:
        out["download_url"] = data["downloadUrl"]
    if "downloadUrlExpiresAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["download_url_expires_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["downloadUrlExpiresAt"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetDatasetResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetDatasetResponse.updated_at required")
    if "tags" in data:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
