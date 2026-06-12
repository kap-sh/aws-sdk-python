"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.report_status_type


class ReportFilter(TypedDict):
    status: NotRequired["aws_sdk_codebuild.types.report_status_type.ReportStatusType"]
    """<p> The status used to filter reports. You can filter using one status only. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_codebuild.types.report_status_type

        out["status"] = (
            aws_sdk_codebuild.types.report_status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportFilter:
    out: ReportFilter = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_codebuild.types.report_status_type

        out["status"] = (
            aws_sdk_codebuild.types.report_status_type.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
