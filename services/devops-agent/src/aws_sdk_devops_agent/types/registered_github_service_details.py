"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredGithubServiceDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.github_repo_owner_type


class RegisteredGithubServiceDetails(TypedDict):
    owner: "str"
    """<p>The GitHub repository owner name.</p>"""
    owner_type: "aws_sdk_devops_agent.types.github_repo_owner_type.GithubRepoOwnerType"
    """<p>The GitHub repository owner type.</p>"""
    target_url: NotRequired["str"]
    """<p>The GitHub Enterprise Server instance URL (absent for github.com).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredGithubServiceDetails) -> dict:
    out: dict = {}
    out["owner"] = value["owner"]
    import aws_sdk_devops_agent.types.github_repo_owner_type

    out["ownerType"] = aws_sdk_devops_agent.types.github_repo_owner_type.serialize_json(
        value["owner_type"]
    )
    if "target_url" in value:
        out["targetUrl"] = value["target_url"]
    return out


def deserialize_json(data: dict) -> RegisteredGithubServiceDetails:
    out: RegisteredGithubServiceDetails = {}  # type: ignore[typeddict-item]
    if "owner" in data:
        out["owner"] = data["owner"]
    else:
        raise DeserializationError("RegisteredGithubServiceDetails.owner required")
    if "ownerType" in data:
        import aws_sdk_devops_agent.types.github_repo_owner_type

        out["owner_type"] = (
            aws_sdk_devops_agent.types.github_repo_owner_type.deserialize_json(
                data["ownerType"]
            )
        )
    else:
        raise DeserializationError("RegisteredGithubServiceDetails.owner_type required")
    if "targetUrl" in data:
        out["target_url"] = data["targetUrl"]
    return out
