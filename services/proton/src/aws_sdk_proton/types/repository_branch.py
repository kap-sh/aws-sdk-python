"""Generated from Smithy shape ``com.amazonaws.proton#RepositoryBranch``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.git_branch_name
    import aws_sdk_proton.types.repository_arn
    import aws_sdk_proton.types.repository_name
    import aws_sdk_proton.types.repository_provider


class RepositoryBranch(TypedDict, closed=True):
    arn: "aws_sdk_proton.types.repository_arn.RepositoryArn"
    """<p>The Amazon Resource Name (ARN) of the linked repository.</p>"""
    provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    name: "aws_sdk_proton.types.repository_name.RepositoryName"
    """<p>The repository name.</p>"""
    branch: "aws_sdk_proton.types.git_branch_name.GitBranchName"
    """<p>The repository branch.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositoryBranch) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["provider"] = value["provider"]
    out["name"] = value["name"]
    out["branch"] = value["branch"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RepositoryBranch:
    out: RepositoryBranch = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("RepositoryBranch.arn required")
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("RepositoryBranch.provider required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RepositoryBranch.name required")
    if "branch" in data:
        out["branch"] = data["branch"]
    else:
        raise DeserializationError("RepositoryBranch.branch required")
    return out
