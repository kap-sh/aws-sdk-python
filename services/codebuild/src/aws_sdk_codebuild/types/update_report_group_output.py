"""Generated from Smithy shape ``com.amazonaws.codebuild#UpdateReportGroupOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.report_group


class UpdateReportGroupOutput(TypedDict):
    report_group: NotRequired["aws_sdk_codebuild.types.report_group.ReportGroup"]
    """<p> Information about the updated report group. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateReportGroupOutput) -> dict:
    out: dict = {}
    if "report_group" in value:
        import aws_sdk_codebuild.types.report_group

        out["reportGroup"] = (
            aws_sdk_codebuild.types.report_group.serialize_aws_json_1_1(
                value["report_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateReportGroupOutput:
    out: UpdateReportGroupOutput = {}  # type: ignore[typeddict-item]
    if "reportGroup" in data:
        import aws_sdk_codebuild.types.report_group

        out["report_group"] = (
            aws_sdk_codebuild.types.report_group.deserialize_aws_json_1_1(
                data["reportGroup"]
            )
        )
    return out
