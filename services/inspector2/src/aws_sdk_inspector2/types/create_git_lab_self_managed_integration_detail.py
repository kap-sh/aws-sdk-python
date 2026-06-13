"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateGitLabSelfManagedIntegrationDetail``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.git_lab_access_token
    import aws_sdk_inspector2.types.instance_url


class CreateGitLabSelfManagedIntegrationDetail(TypedDict):
    instance_url: "aws_sdk_inspector2.types.instance_url.InstanceUrl"
    """<p>The URL of the self-managed GitLab instance.</p>"""
    access_token: "aws_sdk_inspector2.types.git_lab_access_token.GitLabAccessToken"
    """<p>The personal access token used to authenticate with the self-managed GitLab instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGitLabSelfManagedIntegrationDetail) -> dict:
    out: dict = {}
    out["instanceUrl"] = value["instance_url"]
    out["accessToken"] = value["access_token"]
    return out


def deserialize_json(data: dict) -> CreateGitLabSelfManagedIntegrationDetail:
    out: CreateGitLabSelfManagedIntegrationDetail = {}  # type: ignore[typeddict-item]
    if "instanceUrl" in data:
        out["instance_url"] = data["instanceUrl"]
    else:
        raise DeserializationError(
            "CreateGitLabSelfManagedIntegrationDetail.instance_url required"
        )
    if "accessToken" in data:
        out["access_token"] = data["accessToken"]
    else:
        raise DeserializationError(
            "CreateGitLabSelfManagedIntegrationDetail.access_token required"
        )
    return out
