"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetReportGroupsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.report_group_arns
    import aws_sdk_codebuild.types.report_groups


class BatchGetReportGroupsOutput(TypedDict):
    report_groups: NotRequired["aws_sdk_codebuild.types.report_groups.ReportGroups"]
    """<p> The array of report groups returned by <code>BatchGetReportGroups</code>. </p>"""
    report_groups_not_found: NotRequired[
        "aws_sdk_codebuild.types.report_group_arns.ReportGroupArns"
    ]
    """<p> An array of ARNs passed to <code>BatchGetReportGroups</code> that are not associated with a <code>ReportGroup</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetReportGroupsOutput) -> dict:
    out: dict = {}
    if "report_groups" in value:
        import aws_sdk_codebuild.types.report_groups

        out["reportGroups"] = (
            aws_sdk_codebuild.types.report_groups.serialize_aws_json_1_1(
                value["report_groups"]
            )
        )
    if "report_groups_not_found" in value:
        import aws_sdk_codebuild.types.report_group_arns

        out["reportGroupsNotFound"] = (
            aws_sdk_codebuild.types.report_group_arns.serialize_aws_json_1_1(
                value["report_groups_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetReportGroupsOutput:
    out: BatchGetReportGroupsOutput = {}  # type: ignore[typeddict-item]
    if "reportGroups" in data:
        import aws_sdk_codebuild.types.report_groups

        out["report_groups"] = (
            aws_sdk_codebuild.types.report_groups.deserialize_aws_json_1_1(
                data["reportGroups"]
            )
        )
    if "reportGroupsNotFound" in data:
        import aws_sdk_codebuild.types.report_group_arns

        out["report_groups_not_found"] = (
            aws_sdk_codebuild.types.report_group_arns.deserialize_aws_json_1_1(
                data["reportGroupsNotFound"]
            )
        )
    return out
