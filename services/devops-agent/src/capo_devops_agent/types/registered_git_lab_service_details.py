"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredGitLabServiceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.git_lab_token_type


class RegisteredGitLabServiceDetails(TypedDict, closed=True):
    target_url: "str"
    """<p>The GitLab instance URL.</p>"""
    token_type: "capo_devops_agent.types.git_lab_token_type.GitLabTokenType"
    """<p>Type of GitLab access token</p>"""
    group_id: NotRequired["str"]
    """<p>Optional GitLab group ID for group-level access tokens</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredGitLabServiceDetails) -> dict:
    out: dict = {}
    out["targetUrl"] = value["target_url"]
    import capo_devops_agent.types.git_lab_token_type

    out["tokenType"] = capo_devops_agent.types.git_lab_token_type.serialize_json(
        value["token_type"]
    )
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> RegisteredGitLabServiceDetails:
    out: RegisteredGitLabServiceDetails = {}  # type: ignore[typeddict-item]
    if "targetUrl" in data:
        out["target_url"] = data["targetUrl"]
    else:
        raise DeserializationError("RegisteredGitLabServiceDetails.target_url required")
    if "tokenType" in data:
        import capo_devops_agent.types.git_lab_token_type

        out["token_type"] = capo_devops_agent.types.git_lab_token_type.deserialize_json(
            data["tokenType"]
        )
    else:
        raise DeserializationError("RegisteredGitLabServiceDetails.token_type required")
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    return out
