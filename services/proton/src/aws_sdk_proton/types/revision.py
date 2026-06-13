"""Generated from Smithy shape ``com.amazonaws.proton#Revision``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.git_branch_name
    import aws_sdk_proton.types.repository_name
    import aws_sdk_proton.types.repository_provider
    import aws_sdk_proton.types.sha


class Revision(TypedDict):
    repository_name: "aws_sdk_proton.types.repository_name.RepositoryName"
    """<p>The repository name.</p>"""
    repository_provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    sha: "aws_sdk_proton.types.sha.SHA"
    """<p>The secure hash algorithm (SHA) hash for the revision.</p>"""
    directory: "str"
    """<p>The repository directory changed by a commit and push that activated the sync attempt.</p>"""
    branch: "aws_sdk_proton.types.git_branch_name.GitBranchName"
    """<p>The repository branch.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Revision) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["repositoryProvider"] = value["repository_provider"]
    out["sha"] = value["sha"]
    out["directory"] = value["directory"]
    out["branch"] = value["branch"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Revision:
    out: Revision = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("Revision.repository_name required")
    if "repositoryProvider" in data:
        out["repository_provider"] = data["repositoryProvider"]
    else:
        raise DeserializationError("Revision.repository_provider required")
    if "sha" in data:
        out["sha"] = data["sha"]
    else:
        raise DeserializationError("Revision.sha required")
    if "directory" in data:
        out["directory"] = data["directory"]
    else:
        raise DeserializationError("Revision.directory required")
    if "branch" in data:
        out["branch"] = data["branch"]
    else:
        raise DeserializationError("Revision.branch required")
    return out
