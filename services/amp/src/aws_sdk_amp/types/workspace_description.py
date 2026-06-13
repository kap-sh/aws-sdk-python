"""Generated from Smithy shape ``com.amazonaws.amp#WorkspaceDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_amp.types.kms_key_arn
    import aws_sdk_amp.types.tag_map
    import aws_sdk_amp.types.uri
    import aws_sdk_amp.types.workspace_alias
    import aws_sdk_amp.types.workspace_arn
    import aws_sdk_amp.types.workspace_id
    import aws_sdk_amp.types.workspace_status


class WorkspaceDescription(TypedDict):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The unique ID for the workspace. For example, <code>ws-example1-1234-abcd-5678-ef90abcd1234</code>.</p>"""
    alias: NotRequired["aws_sdk_amp.types.workspace_alias.WorkspaceAlias"]
    """<p>The alias that is assigned to this workspace to help identify it. It does not need to be unique.</p>"""
    arn: "aws_sdk_amp.types.workspace_arn.WorkspaceArn"
    """<p>The ARN of the workspace. For example, <code>arn:aws:aps:&lt;region&gt;:123456789012:workspace/ws-example1-1234-abcd-5678-ef90abcd1234</code>.</p>"""
    status: "aws_sdk_amp.types.workspace_status.WorkspaceStatus"
    """<p>The current status of the workspace.</p>"""
    prometheus_endpoint: NotRequired["aws_sdk_amp.types.uri.Uri"]
    """<p>The Prometheus endpoint available for this workspace. For example, <code>https://aps-workspaces.&lt;region&gt;.amazonaws.com/workspaces/ws-example1-1234-abcd-5678-ef90abcd1234/api/v1/</code>.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the workspace was created.</p>"""
    tags: NotRequired["aws_sdk_amp.types.tag_map.TagMap"]
    """<p>The list of tag keys and values that are associated with the workspace.</p>"""
    kms_key_arn: NotRequired["aws_sdk_amp.types.kms_key_arn.KmsKeyArn"]
    """<p>(optional) If the workspace was created with a customer managed KMS key, the ARN for the key used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceDescription) -> dict:
    out: dict = {}
    out["workspaceId"] = value["workspace_id"]
    if "alias" in value:
        out["alias"] = value["alias"]
    out["arn"] = value["arn"]
    import aws_sdk_amp.types.workspace_status

    out["status"] = aws_sdk_amp.types.workspace_status.serialize_json(value["status"])
    if "prometheus_endpoint" in value:
        out["prometheusEndpoint"] = value["prometheus_endpoint"]
    import aws_sdk_amp.types._prelude.timestamp

    out["createdAt"] = aws_sdk_amp.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "tags" in value:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.serialize_json(value["tags"])
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> WorkspaceDescription:
    out: WorkspaceDescription = {}  # type: ignore[typeddict-item]
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError("WorkspaceDescription.workspace_id required")
    if "alias" in data:
        out["alias"] = data["alias"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("WorkspaceDescription.arn required")
    if "status" in data:
        import aws_sdk_amp.types.workspace_status

        out["status"] = aws_sdk_amp.types.workspace_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("WorkspaceDescription.status required")
    if "prometheusEndpoint" in data:
        out["prometheus_endpoint"] = data["prometheusEndpoint"]
    if "createdAt" in data:
        import aws_sdk_amp.types._prelude.timestamp

        out["created_at"] = aws_sdk_amp.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("WorkspaceDescription.created_at required")
    if "tags" in data:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.deserialize_json(data["tags"])
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
