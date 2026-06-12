"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportGroupTrendRawDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.report_with_raw_data

ReportGroupTrendRawDataList: TypeAlias = list[
    "aws_sdk_codebuild.types.report_with_raw_data.ReportWithRawData"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportGroupTrendRawDataList) -> list:
    import aws_sdk_codebuild.types.report_with_raw_data

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codebuild.types.report_with_raw_data.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReportGroupTrendRawDataList:
    import aws_sdk_codebuild.types.report_with_raw_data

    out: ReportGroupTrendRawDataList = []
    for item in data:
        out.append(
            aws_sdk_codebuild.types.report_with_raw_data.deserialize_aws_json_1_1(item)
        )
    return out
