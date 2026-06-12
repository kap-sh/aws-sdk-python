"""Generated from Smithy shape ``com.amazonaws.codebuild#Reports``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.report

Reports: TypeAlias = list["aws_sdk_codebuild.types.report.Report"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Reports) -> list:
    import aws_sdk_codebuild.types.report

    out: list = []
    for item in value:
        out.append(aws_sdk_codebuild.types.report.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Reports:
    import aws_sdk_codebuild.types.report

    out: Reports = []
    for item in data:
        out.append(aws_sdk_codebuild.types.report.deserialize_aws_json_1_1(item))
    return out
