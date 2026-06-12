"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildsNotDeleted``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_not_deleted

BuildsNotDeleted: TypeAlias = list[
    "aws_sdk_codebuild.types.build_not_deleted.BuildNotDeleted"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildsNotDeleted) -> list:
    import aws_sdk_codebuild.types.build_not_deleted

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codebuild.types.build_not_deleted.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BuildsNotDeleted:
    import aws_sdk_codebuild.types.build_not_deleted

    out: BuildsNotDeleted = []
    for item in data:
        out.append(
            aws_sdk_codebuild.types.build_not_deleted.deserialize_aws_json_1_1(item)
        )
    return out
