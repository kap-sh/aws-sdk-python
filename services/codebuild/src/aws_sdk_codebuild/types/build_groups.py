"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_group

BuildGroups: TypeAlias = list["aws_sdk_codebuild.types.build_group.BuildGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildGroups) -> list:
    import aws_sdk_codebuild.types.build_group

    out: list = []
    for item in value:
        out.append(aws_sdk_codebuild.types.build_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BuildGroups:
    import aws_sdk_codebuild.types.build_group

    out: BuildGroups = []
    for item in data:
        out.append(aws_sdk_codebuild.types.build_group.deserialize_aws_json_1_1(item))
    return out
