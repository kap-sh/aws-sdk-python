"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.report_group

ReportGroups: TypeAlias = list["aws_sdk_codebuild.types.report_group.ReportGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportGroups) -> list:
    import aws_sdk_codebuild.types.report_group

    out: list = []
    for item in value:
        out.append(aws_sdk_codebuild.types.report_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ReportGroups:
    import aws_sdk_codebuild.types.report_group

    out: ReportGroups = []
    for item in data:
        out.append(aws_sdk_codebuild.types.report_group.deserialize_aws_json_1_1(item))
    return out
