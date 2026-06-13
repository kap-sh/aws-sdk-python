"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceSyncConfigInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.git_branch_name
    import aws_sdk_proton.types.ops_file_path
    import aws_sdk_proton.types.repository_name
    import aws_sdk_proton.types.repository_provider
    import aws_sdk_proton.types.resource_name


class UpdateServiceSyncConfigInput(TypedDict):
    service_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service the Proton Ops file is for.</p>"""
    repository_provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider"
    """<p>The name of the repository provider where the Proton Ops file is found.</p>"""
    repository_name: "aws_sdk_proton.types.repository_name.RepositoryName"
    """<p>The name of the repository where the Proton Ops file is found.</p>"""
    branch: "aws_sdk_proton.types.git_branch_name.GitBranchName"
    """<p>The name of the code repository branch where the Proton Ops file is found.</p>"""
    file_path: "aws_sdk_proton.types.ops_file_path.OpsFilePath"
    """<p>The path to the Proton Ops file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceSyncConfigInput) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    out["repositoryProvider"] = value["repository_provider"]
    out["repositoryName"] = value["repository_name"]
    out["branch"] = value["branch"]
    out["filePath"] = value["file_path"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceSyncConfigInput:
    out: UpdateServiceSyncConfigInput = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError("UpdateServiceSyncConfigInput.service_name required")
    if "repositoryProvider" in data:
        out["repository_provider"] = data["repositoryProvider"]
    else:
        raise DeserializationError(
            "UpdateServiceSyncConfigInput.repository_provider required"
        )
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "UpdateServiceSyncConfigInput.repository_name required"
        )
    if "branch" in data:
        out["branch"] = data["branch"]
    else:
        raise DeserializationError("UpdateServiceSyncConfigInput.branch required")
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("UpdateServiceSyncConfigInput.file_path required")
    return out
