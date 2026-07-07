"""Generated from Smithy shape ``com.amazonaws.codestarconnections#GetRepositorySyncStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.branch_name
    import aws_sdk_codestar_connections.types.repository_link_id
    import aws_sdk_codestar_connections.types.sync_configuration_type


class GetRepositorySyncStatusInput(TypedDict, closed=True):
    branch: "aws_sdk_codestar_connections.types.branch_name.BranchName"
    """<p>The branch of the repository link for the requested repository sync status.</p>"""
    repository_link_id: (
        "aws_sdk_codestar_connections.types.repository_link_id.RepositoryLinkId"
    )
    """<p>The repository link ID for the requested repository sync status.</p>"""
    sync_type: "aws_sdk_codestar_connections.types.sync_configuration_type.SyncConfigurationType"
    """<p>The sync type of the requested sync status.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRepositorySyncStatusInput) -> dict:
    out: dict = {}
    out["Branch"] = value["branch"]
    out["RepositoryLinkId"] = value["repository_link_id"]
    import aws_sdk_codestar_connections.types.sync_configuration_type

    out["SyncType"] = (
        aws_sdk_codestar_connections.types.sync_configuration_type.serialize_aws_json_1_0(
            value["sync_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRepositorySyncStatusInput:
    out: GetRepositorySyncStatusInput = {}  # type: ignore[typeddict-item]
    if "Branch" in data:
        out["branch"] = data["Branch"]
    else:
        raise DeserializationError("GetRepositorySyncStatusInput.branch required")
    if "RepositoryLinkId" in data:
        out["repository_link_id"] = data["RepositoryLinkId"]
    else:
        raise DeserializationError(
            "GetRepositorySyncStatusInput.repository_link_id required"
        )
    if "SyncType" in data:
        import aws_sdk_codestar_connections.types.sync_configuration_type

        out["sync_type"] = (
            aws_sdk_codestar_connections.types.sync_configuration_type.deserialize_aws_json_1_0(
                data["SyncType"]
            )
        )
    else:
        raise DeserializationError("GetRepositorySyncStatusInput.sync_type required")
    return out
