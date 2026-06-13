"""Generated from Smithy shape ``com.amazonaws.proton#GetRepositorySyncStatusInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.git_branch_name
    import aws_sdk_proton.types.repository_name
    import aws_sdk_proton.types.repository_provider
    import aws_sdk_proton.types.sync_type


class GetRepositorySyncStatusInput(TypedDict):
    repository_name: "aws_sdk_proton.types.repository_name.RepositoryName"
    """<p>The repository name.</p>"""
    repository_provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    branch: "aws_sdk_proton.types.git_branch_name.GitBranchName"
    """<p>The repository branch.</p>"""
    sync_type: "aws_sdk_proton.types.sync_type.SyncType"
    """<p>The repository sync type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRepositorySyncStatusInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["repositoryProvider"] = value["repository_provider"]
    out["branch"] = value["branch"]
    out["syncType"] = value["sync_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRepositorySyncStatusInput:
    out: GetRepositorySyncStatusInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "GetRepositorySyncStatusInput.repository_name required"
        )
    if "repositoryProvider" in data:
        out["repository_provider"] = data["repositoryProvider"]
    else:
        raise DeserializationError(
            "GetRepositorySyncStatusInput.repository_provider required"
        )
    if "branch" in data:
        out["branch"] = data["branch"]
    else:
        raise DeserializationError("GetRepositorySyncStatusInput.branch required")
    if "syncType" in data:
        out["sync_type"] = data["syncType"]
    else:
        raise DeserializationError("GetRepositorySyncStatusInput.sync_type required")
    return out
