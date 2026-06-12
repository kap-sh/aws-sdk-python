"""Generated from Smithy shape ``com.amazonaws.workspaces#StandbyWorkspace``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.data_replication
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.tag_list
    import aws_sdk_workspaces.types.volume_encryption_key
    import aws_sdk_workspaces.types.workspace_id


class StandbyWorkspace(TypedDict):
    primary_workspace_id: "aws_sdk_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the standby WorkSpace.</p>"""
    volume_encryption_key: NotRequired[
        "aws_sdk_workspaces.types.volume_encryption_key.VolumeEncryptionKey"
    ]
    """<p>The volume encryption key of the standby WorkSpace.</p>"""
    directory_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for the standby WorkSpace.</p>"""
    tags: NotRequired["aws_sdk_workspaces.types.tag_list.TagList"]
    """<p>The tags associated with the standby WorkSpace.</p>"""
    data_replication: NotRequired[
        "aws_sdk_workspaces.types.data_replication.DataReplication"
    ]
    """<p>Indicates whether data replication is enabled, and if enabled, the type of data replication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StandbyWorkspace) -> dict:
    out: dict = {}
    out["PrimaryWorkspaceId"] = value["primary_workspace_id"]
    if "volume_encryption_key" in value:
        out["VolumeEncryptionKey"] = value["volume_encryption_key"]
    out["DirectoryId"] = value["directory_id"]
    if "tags" in value:
        import aws_sdk_workspaces.types.tag_list

        out["Tags"] = aws_sdk_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "data_replication" in value:
        import aws_sdk_workspaces.types.data_replication

        out["DataReplication"] = (
            aws_sdk_workspaces.types.data_replication.serialize_aws_json_1_1(
                value["data_replication"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StandbyWorkspace:
    out: StandbyWorkspace = {}  # type: ignore[typeddict-item]
    if "PrimaryWorkspaceId" in data:
        out["primary_workspace_id"] = data["PrimaryWorkspaceId"]
    else:
        raise DeserializationError("StandbyWorkspace.primary_workspace_id required")
    if "VolumeEncryptionKey" in data:
        out["volume_encryption_key"] = data["VolumeEncryptionKey"]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("StandbyWorkspace.directory_id required")
    if "Tags" in data:
        import aws_sdk_workspaces.types.tag_list

        out["tags"] = aws_sdk_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "DataReplication" in data:
        import aws_sdk_workspaces.types.data_replication

        out["data_replication"] = (
            aws_sdk_workspaces.types.data_replication.deserialize_aws_json_1_1(
                data["DataReplication"]
            )
        )
    return out
