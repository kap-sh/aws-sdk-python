"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitBranchFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.git_branch_pattern_list


class GitBranchFilterCriteria(TypedDict, closed=True):
    includes: NotRequired[
        "aws_sdk_codepipeline.types.git_branch_pattern_list.GitBranchPatternList"
    ]
    """<p>The list of patterns of Git branches that, when a commit is pushed, are to be included as criteria that starts the pipeline.</p>"""
    excludes: NotRequired[
        "aws_sdk_codepipeline.types.git_branch_pattern_list.GitBranchPatternList"
    ]
    """<p>The list of patterns of Git branches that, when a commit is pushed, are to be excluded from starting the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitBranchFilterCriteria) -> dict:
    out: dict = {}
    if "includes" in value:
        import aws_sdk_codepipeline.types.git_branch_pattern_list

        out["includes"] = (
            aws_sdk_codepipeline.types.git_branch_pattern_list.serialize_aws_json_1_1(
                value["includes"]
            )
        )
    if "excludes" in value:
        import aws_sdk_codepipeline.types.git_branch_pattern_list

        out["excludes"] = (
            aws_sdk_codepipeline.types.git_branch_pattern_list.serialize_aws_json_1_1(
                value["excludes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GitBranchFilterCriteria:
    out: GitBranchFilterCriteria = {}  # type: ignore[typeddict-item]
    if "includes" in data:
        import aws_sdk_codepipeline.types.git_branch_pattern_list

        out["includes"] = (
            aws_sdk_codepipeline.types.git_branch_pattern_list.deserialize_aws_json_1_1(
                data["includes"]
            )
        )
    if "excludes" in data:
        import aws_sdk_codepipeline.types.git_branch_pattern_list

        out["excludes"] = (
            aws_sdk_codepipeline.types.git_branch_pattern_list.deserialize_aws_json_1_1(
                data["excludes"]
            )
        )
    return out
