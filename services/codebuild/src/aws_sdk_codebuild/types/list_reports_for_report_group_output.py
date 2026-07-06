"""Generated from Smithy shape ``com.amazonaws.codebuild#ListReportsForReportGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.report_arns
    import aws_sdk_codebuild.types.string


class ListReportsForReportGroupOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>"""
    reports: NotRequired["aws_sdk_codebuild.types.report_arns.ReportArns"]
    """<p> The list of report ARNs. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReportsForReportGroupOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "reports" in value:
        import aws_sdk_codebuild.types.report_arns

        out["reports"] = aws_sdk_codebuild.types.report_arns.serialize_aws_json_1_1(
            value["reports"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReportsForReportGroupOutput:
    out: ListReportsForReportGroupOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "reports" in data:
        import aws_sdk_codebuild.types.report_arns

        out["reports"] = aws_sdk_codebuild.types.report_arns.deserialize_aws_json_1_1(
            data["reports"]
        )
    return out
