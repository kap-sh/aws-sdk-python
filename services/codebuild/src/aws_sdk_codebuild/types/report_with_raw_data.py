"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportWithRawData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.string


class ReportWithRawData(TypedDict, closed=True):
    report_arn: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the report.</p>"""
    data: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The value of the requested data field from the report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportWithRawData) -> dict:
    out: dict = {}
    if "report_arn" in value:
        out["reportArn"] = value["report_arn"]
    if "data" in value:
        out["data"] = value["data"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportWithRawData:
    out: ReportWithRawData = {}  # type: ignore[typeddict-item]
    if "reportArn" in data:
        out["report_arn"] = data["reportArn"]
    if "data" in data:
        out["data"] = data["data"]
    return out
