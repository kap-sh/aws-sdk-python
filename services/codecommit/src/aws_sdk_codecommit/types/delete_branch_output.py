"""Generated from Smithy shape ``com.amazonaws.codecommit#DeleteBranchOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.branch_info


class DeleteBranchOutput(TypedDict):
    deleted_branch: NotRequired["aws_sdk_codecommit.types.branch_info.BranchInfo"]
    """<p>Information about the branch deleted by the operation, including the branch name and the commit ID that was the tip of the branch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBranchOutput) -> dict:
    out: dict = {}
    if "deleted_branch" in value:
        import aws_sdk_codecommit.types.branch_info

        out["deletedBranch"] = (
            aws_sdk_codecommit.types.branch_info.serialize_aws_json_1_1(
                value["deleted_branch"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBranchOutput:
    out: DeleteBranchOutput = {}  # type: ignore[typeddict-item]
    if "deletedBranch" in data:
        import aws_sdk_codecommit.types.branch_info

        out["deleted_branch"] = (
            aws_sdk_codecommit.types.branch_info.deserialize_aws_json_1_1(
                data["deletedBranch"]
            )
        )
    return out
