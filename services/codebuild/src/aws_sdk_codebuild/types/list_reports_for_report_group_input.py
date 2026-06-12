"""Generated from Smithy shape ``com.amazonaws.codebuild#ListReportsForReportGroupInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.page_size
    import aws_sdk_codebuild.types.report_filter
    import aws_sdk_codebuild.types.sort_order_type
    import aws_sdk_codebuild.types.string


class ListReportsForReportGroupInput(TypedDict):
    report_group_arn: "aws_sdk_codebuild.types.string.String"
    """<p> The ARN of the report group for which you want to return report ARNs. </p>"""
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>"""
    sort_order: NotRequired["aws_sdk_codebuild.types.sort_order_type.SortOrderType"]
    """<p> Use to specify whether the results are returned in ascending or descending order. </p>"""
    max_results: NotRequired["aws_sdk_codebuild.types.page_size.PageSize"]
    """<p> The maximum number of paginated reports in this report group returned per response. Use <code>nextToken</code> to iterate pages in the list of returned <code>Report</code> objects. The default value is 100. </p>"""
    filter: NotRequired["aws_sdk_codebuild.types.report_filter.ReportFilter"]
    """<p> A <code>ReportFilter</code> object used to filter the returned reports. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReportsForReportGroupInput) -> dict:
    out: dict = {}
    out["reportGroupArn"] = value["report_group_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sort_order" in value:
        import aws_sdk_codebuild.types.sort_order_type

        out["sortOrder"] = (
            aws_sdk_codebuild.types.sort_order_type.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter" in value:
        import aws_sdk_codebuild.types.report_filter

        out["filter"] = aws_sdk_codebuild.types.report_filter.serialize_aws_json_1_1(
            value["filter"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReportsForReportGroupInput:
    out: ListReportsForReportGroupInput = {}  # type: ignore[typeddict-item]
    if "reportGroupArn" in data:
        out["report_group_arn"] = data["reportGroupArn"]
    else:
        raise DeserializationError(
            "ListReportsForReportGroupInput.report_group_arn required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sortOrder" in data:
        import aws_sdk_codebuild.types.sort_order_type

        out["sort_order"] = (
            aws_sdk_codebuild.types.sort_order_type.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filter" in data:
        import aws_sdk_codebuild.types.report_filter

        out["filter"] = aws_sdk_codebuild.types.report_filter.deserialize_aws_json_1_1(
            data["filter"]
        )
    return out
