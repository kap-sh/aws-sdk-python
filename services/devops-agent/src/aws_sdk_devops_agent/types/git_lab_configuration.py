"""Generated from Smithy shape ``com.amazonaws.devopsagent#GitLabConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError


class GitLabConfiguration(TypedDict):
    project_id: "str"
    """<p>GitLab numeric project ID.</p>"""
    project_path: "str"
    """<p>Full GitLab project path (e.g., namespace/project-name).</p>"""
    instance_identifier: NotRequired["str"]
    """<p>GitLab instance identifier (e.g., gitlab.com or e2e.gamma.dev.us-east-1.gitlab.falco.ai.aws.dev)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitLabConfiguration) -> dict:
    out: dict = {}
    out["projectId"] = value["project_id"]
    out["projectPath"] = value["project_path"]
    if "instance_identifier" in value:
        out["instanceIdentifier"] = value["instance_identifier"]
    return out


def deserialize_json(data: dict) -> GitLabConfiguration:
    out: GitLabConfiguration = {}  # type: ignore[typeddict-item]
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("GitLabConfiguration.project_id required")
    if "projectPath" in data:
        out["project_path"] = data["projectPath"]
    else:
        raise DeserializationError("GitLabConfiguration.project_path required")
    if "instanceIdentifier" in data:
        out["instance_identifier"] = data["instanceIdentifier"]
    return out
