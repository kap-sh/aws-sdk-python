"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSkillGitSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_skill_git_auth
    import aws_sdk_bedrock_agentcore_control.types.harness_skill_git_url


class HarnessSkillGitSource(TypedDict, closed=True):
    url: "aws_sdk_bedrock_agentcore_control.types.harness_skill_git_url.HarnessSkillGitUrl"
    """<p>The HTTPS URL of the git repository.</p>"""
    path: NotRequired["str"]
    """<p>Subdirectory within the repository containing the skill.</p>"""
    auth: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_skill_git_auth.HarnessSkillGitAuth"
    ]
    """<p>Authentication configuration for private repositories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSkillGitSource) -> dict:
    out: dict = {}
    out["url"] = value["url"]
    if "path" in value:
        out["path"] = value["path"]
    if "auth" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_skill_git_auth

        out["auth"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_skill_git_auth.serialize_json(
                value["auth"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessSkillGitSource:
    out: HarnessSkillGitSource = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    else:
        raise DeserializationError("HarnessSkillGitSource.url required")
    if "path" in data:
        out["path"] = data["path"]
    if "auth" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_skill_git_auth

        out["auth"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_skill_git_auth.deserialize_json(
                data["auth"]
            )
        )
    return out
