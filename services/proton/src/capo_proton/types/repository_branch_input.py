"""Generated from Smithy shape ``com.amazonaws.proton#RepositoryBranchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.git_branch_name
    import capo_proton.types.repository_name
    import capo_proton.types.repository_provider


class RepositoryBranchInput(TypedDict, closed=True):
    provider: "capo_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    name: "capo_proton.types.repository_name.RepositoryName"
    """<p>The repository name.</p>"""
    branch: "capo_proton.types.git_branch_name.GitBranchName"
    """<p>The repository branch.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositoryBranchInput) -> dict:
    out: dict = {}
    out["provider"] = value["provider"]
    out["name"] = value["name"]
    out["branch"] = value["branch"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RepositoryBranchInput:
    out: RepositoryBranchInput = {}  # type: ignore[typeddict-item]
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("RepositoryBranchInput.provider required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RepositoryBranchInput.name required")
    if "branch" in data:
        out["branch"] = data["branch"]
    else:
        raise DeserializationError("RepositoryBranchInput.branch required")
    return out
