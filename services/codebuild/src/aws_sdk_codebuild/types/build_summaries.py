"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_summary

BuildSummaries: TypeAlias = list["aws_sdk_codebuild.types.build_summary.BuildSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildSummaries) -> list:
    import aws_sdk_codebuild.types.build_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_codebuild.types.build_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BuildSummaries:
    import aws_sdk_codebuild.types.build_summary

    out: BuildSummaries = []
    for item in data:
        out.append(aws_sdk_codebuild.types.build_summary.deserialize_aws_json_1_1(item))
    return out
