"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitTagPatternList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.git_tag_name_pattern

GitTagPatternList: TypeAlias = list[
    "capo_codepipeline.types.git_tag_name_pattern.GitTagNamePattern"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitTagPatternList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GitTagPatternList:
    return list(data)
