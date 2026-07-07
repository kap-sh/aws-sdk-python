"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateDefaultBranchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.branch_name
    import aws_sdk_codecommit.types.repository_name


class UpdateDefaultBranchInput(TypedDict, closed=True):
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository for which you want to set or change the default branch.</p>"""
    default_branch_name: "aws_sdk_codecommit.types.branch_name.BranchName"
    """<p>The name of the branch to set as the default branch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDefaultBranchInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["defaultBranchName"] = value["default_branch_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDefaultBranchInput:
    out: UpdateDefaultBranchInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("UpdateDefaultBranchInput.repository_name required")
    if "defaultBranchName" in data:
        out["default_branch_name"] = data["defaultBranchName"]
    else:
        raise DeserializationError(
            "UpdateDefaultBranchInput.default_branch_name required"
        )
    return out
