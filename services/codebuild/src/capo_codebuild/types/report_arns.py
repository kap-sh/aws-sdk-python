"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string

ReportArns: TypeAlias = list["capo_codebuild.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ReportArns:
    return list(data)
