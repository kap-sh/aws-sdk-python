"""Generated from Smithy shape ``com.amazonaws.securityagent#GitHubRepositoryResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.git_hub_owner
    import aws_sdk_securityagent.types.provider_resource_name


class GitHubRepositoryResource(TypedDict, closed=True):
    name: "aws_sdk_securityagent.types.provider_resource_name.ProviderResourceName"
    """<p>The name of the GitHub repository.</p>"""
    owner: "aws_sdk_securityagent.types.git_hub_owner.GitHubOwner"
    """<p>The owner of the GitHub repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitHubRepositoryResource) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["owner"] = value["owner"]
    return out


def deserialize_json(data: dict) -> GitHubRepositoryResource:
    out: GitHubRepositoryResource = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GitHubRepositoryResource.name required")
    if "owner" in data:
        out["owner"] = data["owner"]
    else:
        raise DeserializationError("GitHubRepositoryResource.owner required")
    return out
