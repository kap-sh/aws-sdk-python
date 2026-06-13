"""Generated from Smithy shape ``com.amazonaws.devopsagent#GitLabDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.git_lab_token_type
    import aws_sdk_devops_agent.types.token_value


class GitLabDetails(TypedDict):
    target_url: "str"
    """<p>GitLab instance URL (e.g., https://gitlab.com or self-hosted instance).</p>"""
    token_type: "aws_sdk_devops_agent.types.git_lab_token_type.GitLabTokenType"
    """<p>Type of GitLab access token</p>"""
    token_value: "aws_sdk_devops_agent.types.token_value.TokenValue"
    """<p>GitLab access token value</p>"""
    group_id: NotRequired["str"]
    """<p>Optional GitLab group ID for group-level access tokens</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitLabDetails) -> dict:
    out: dict = {}
    out["targetUrl"] = value["target_url"]
    import aws_sdk_devops_agent.types.git_lab_token_type

    out["tokenType"] = aws_sdk_devops_agent.types.git_lab_token_type.serialize_json(
        value["token_type"]
    )
    out["tokenValue"] = value["token_value"]
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> GitLabDetails:
    out: GitLabDetails = {}  # type: ignore[typeddict-item]
    if "targetUrl" in data:
        out["target_url"] = data["targetUrl"]
    else:
        raise DeserializationError("GitLabDetails.target_url required")
    if "tokenType" in data:
        import aws_sdk_devops_agent.types.git_lab_token_type

        out["token_type"] = (
            aws_sdk_devops_agent.types.git_lab_token_type.deserialize_json(
                data["tokenType"]
            )
        )
    else:
        raise DeserializationError("GitLabDetails.token_type required")
    if "tokenValue" in data:
        out["token_value"] = data["tokenValue"]
    else:
        raise DeserializationError("GitLabDetails.token_value required")
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    return out
