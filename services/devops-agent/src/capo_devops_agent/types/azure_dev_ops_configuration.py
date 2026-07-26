"""Generated from Smithy shape ``com.amazonaws.devopsagent#AzureDevOpsConfiguration``."""

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError


class AzureDevOpsConfiguration(TypedDict, closed=True):
    organization_name: "str"
    """<p>Azure DevOps organization name.</p>"""
    project_id: "str"
    """<p>Azure DevOps project ID.</p>"""
    project_name: "str"
    """<p>Azure DevOps project name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureDevOpsConfiguration) -> dict:
    out: dict = {}
    out["organizationName"] = value["organization_name"]
    out["projectId"] = value["project_id"]
    out["projectName"] = value["project_name"]
    return out


def deserialize_json(data: dict) -> AzureDevOpsConfiguration:
    out: AzureDevOpsConfiguration = {}  # type: ignore[typeddict-item]
    if "organizationName" in data:
        out["organization_name"] = data["organizationName"]
    else:
        raise DeserializationError(
            "AzureDevOpsConfiguration.organization_name required"
        )
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("AzureDevOpsConfiguration.project_id required")
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("AzureDevOpsConfiguration.project_name required")
    return out
