"""Generated from Smithy shape ``com.amazonaws.devopsagent#GitHubConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.github_repo_owner_type


class GitHubConfiguration(TypedDict, closed=True):
    repo_name: "str"
    """<p>Associated Github repo name</p>"""
    repo_id: "str"
    """<p>Associated Github repo ID</p>"""
    owner: "str"
    """<p>The GitHub repository owner name.</p>"""
    owner_type: "aws_sdk_devops_agent.types.github_repo_owner_type.GithubRepoOwnerType"
    instance_identifier: NotRequired["str"]
    """<p>GitHub instance identifier (e.g., github.com or github.enterprise.com)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitHubConfiguration) -> dict:
    out: dict = {}
    out["repoName"] = value["repo_name"]
    out["repoId"] = value["repo_id"]
    out["owner"] = value["owner"]
    import aws_sdk_devops_agent.types.github_repo_owner_type

    out["ownerType"] = aws_sdk_devops_agent.types.github_repo_owner_type.serialize_json(
        value["owner_type"]
    )
    if "instance_identifier" in value:
        out["instanceIdentifier"] = value["instance_identifier"]
    return out


def deserialize_json(data: dict) -> GitHubConfiguration:
    out: GitHubConfiguration = {}  # type: ignore[typeddict-item]
    if "repoName" in data:
        out["repo_name"] = data["repoName"]
    else:
        raise DeserializationError("GitHubConfiguration.repo_name required")
    if "repoId" in data:
        out["repo_id"] = data["repoId"]
    else:
        raise DeserializationError("GitHubConfiguration.repo_id required")
    if "owner" in data:
        out["owner"] = data["owner"]
    else:
        raise DeserializationError("GitHubConfiguration.owner required")
    if "ownerType" in data:
        import aws_sdk_devops_agent.types.github_repo_owner_type

        out["owner_type"] = (
            aws_sdk_devops_agent.types.github_repo_owner_type.deserialize_json(
                data["ownerType"]
            )
        )
    else:
        raise DeserializationError("GitHubConfiguration.owner_type required")
    if "instanceIdentifier" in data:
        out["instance_identifier"] = data["instanceIdentifier"]
    return out
