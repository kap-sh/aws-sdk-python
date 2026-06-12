"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DevEnvironmentRepositorySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.source_repository_branch_string
    import aws_sdk_codecatalyst.types.source_repository_name_string


class DevEnvironmentRepositorySummary(TypedDict):
    repository_name: "aws_sdk_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString"
    """<p>The name of the source repository.</p>"""
    branch_name: NotRequired[
        "aws_sdk_codecatalyst.types.source_repository_branch_string.SourceRepositoryBranchString"
    ]
    """<p>The name of the branch in a source repository cloned into the Dev Environment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DevEnvironmentRepositorySummary) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    return out


def deserialize_json(data: dict) -> DevEnvironmentRepositorySummary:
    out: DevEnvironmentRepositorySummary = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "DevEnvironmentRepositorySummary.repository_name required"
        )
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    return out
