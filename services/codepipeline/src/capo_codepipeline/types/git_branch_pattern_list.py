"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitBranchPatternList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.git_branch_name_pattern

GitBranchPatternList: TypeAlias = list[
    "capo_codepipeline.types.git_branch_name_pattern.GitBranchNamePattern"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitBranchPatternList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GitBranchPatternList:
    return list(data)
