"""Generated from Smithy shape ``com.amazonaws.amp#CreateWorkspaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.kms_key_arn
    import aws_sdk_amp.types.tag_map
    import aws_sdk_amp.types.workspace_arn
    import aws_sdk_amp.types.workspace_id
    import aws_sdk_amp.types.workspace_status


class CreateWorkspaceResponse(TypedDict):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The unique ID for the new workspace.</p>"""
    arn: "aws_sdk_amp.types.workspace_arn.WorkspaceArn"
    """<p>The ARN for the new workspace.</p>"""
    status: "aws_sdk_amp.types.workspace_status.WorkspaceStatus"
    """<p>The current status of the new workspace. Immediately after you create the workspace, the status is usually <code>CREATING</code>.</p>"""
    tags: NotRequired["aws_sdk_amp.types.tag_map.TagMap"]
    """<p>The list of tag keys and values that are associated with the workspace.</p>"""
    kms_key_arn: NotRequired["aws_sdk_amp.types.kms_key_arn.KmsKeyArn"]
    """<p>(optional) If the workspace was created with a customer managed KMS key, the ARN for the key used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceResponse) -> dict:
    out: dict = {}
    out["workspaceId"] = value["workspace_id"]
    out["arn"] = value["arn"]
    import aws_sdk_amp.types.workspace_status

    out["status"] = aws_sdk_amp.types.workspace_status.serialize_json(value["status"])
    if "tags" in value:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.serialize_json(value["tags"])
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceResponse:
    out: CreateWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError("CreateWorkspaceResponse.workspace_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateWorkspaceResponse.arn required")
    if "status" in data:
        import aws_sdk_amp.types.workspace_status

        out["status"] = aws_sdk_amp.types.workspace_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateWorkspaceResponse.status required")
    if "tags" in data:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.deserialize_json(data["tags"])
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
