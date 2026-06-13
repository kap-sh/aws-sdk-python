"""Generated from Smithy shape ``com.amazonaws.proton#RepositorySyncDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.git_branch_name


class RepositorySyncDefinition(TypedDict):
    target: "str"
    """<p>The resource that is synced to.</p>"""
    parent: "str"
    """<p>The resource that is synced from.</p>"""
    branch: "aws_sdk_proton.types.git_branch_name.GitBranchName"
    """<p>The repository branch.</p>"""
    directory: "str"
    """<p>The directory in the repository.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncDefinition) -> dict:
    out: dict = {}
    out["target"] = value["target"]
    out["parent"] = value["parent"]
    out["branch"] = value["branch"]
    out["directory"] = value["directory"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RepositorySyncDefinition:
    out: RepositorySyncDefinition = {}  # type: ignore[typeddict-item]
    if "target" in data:
        out["target"] = data["target"]
    else:
        raise DeserializationError("RepositorySyncDefinition.target required")
    if "parent" in data:
        out["parent"] = data["parent"]
    else:
        raise DeserializationError("RepositorySyncDefinition.parent required")
    if "branch" in data:
        out["branch"] = data["branch"]
    else:
        raise DeserializationError("RepositorySyncDefinition.branch required")
    if "directory" in data:
        out["directory"] = data["directory"]
    else:
        raise DeserializationError("RepositorySyncDefinition.directory required")
    return out
