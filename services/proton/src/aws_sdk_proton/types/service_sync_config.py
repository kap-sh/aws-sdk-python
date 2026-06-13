"""Generated from Smithy shape ``com.amazonaws.proton#ServiceSyncConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.git_branch_name
    import aws_sdk_proton.types.ops_file_path
    import aws_sdk_proton.types.repository_name
    import aws_sdk_proton.types.repository_provider
    import aws_sdk_proton.types.resource_name


class ServiceSyncConfig(TypedDict):
    service_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service that the service instance is added to.</p>"""
    repository_provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider"
    """<p>The name of the repository provider that holds the repository Proton will sync with.</p>"""
    repository_name: "aws_sdk_proton.types.repository_name.RepositoryName"
    """<p>The name of the code repository that holds the service code Proton will sync with.</p>"""
    branch: "aws_sdk_proton.types.git_branch_name.GitBranchName"
    """<p>The name of the code repository branch that holds the service code Proton will sync with.</p>"""
    file_path: "aws_sdk_proton.types.ops_file_path.OpsFilePath"
    """<p>The file path to the service sync configuration file.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceSyncConfig) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    out["repositoryProvider"] = value["repository_provider"]
    out["repositoryName"] = value["repository_name"]
    out["branch"] = value["branch"]
    out["filePath"] = value["file_path"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceSyncConfig:
    out: ServiceSyncConfig = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError("ServiceSyncConfig.service_name required")
    if "repositoryProvider" in data:
        out["repository_provider"] = data["repositoryProvider"]
    else:
        raise DeserializationError("ServiceSyncConfig.repository_provider required")
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("ServiceSyncConfig.repository_name required")
    if "branch" in data:
        out["branch"] = data["branch"]
    else:
        raise DeserializationError("ServiceSyncConfig.branch required")
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("ServiceSyncConfig.file_path required")
    return out
