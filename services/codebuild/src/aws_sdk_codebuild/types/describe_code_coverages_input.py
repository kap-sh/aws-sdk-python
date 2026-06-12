"""Generated from Smithy shape ``com.amazonaws.codebuild#DescribeCodeCoveragesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.page_size
    import aws_sdk_codebuild.types.percentage
    import aws_sdk_codebuild.types.report_code_coverage_sort_by_type
    import aws_sdk_codebuild.types.sort_order_type
    import aws_sdk_codebuild.types.string


class DescribeCodeCoveragesInput(TypedDict):
    report_arn: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p> The ARN of the report for which test cases are returned. </p>"""
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous call to <code>DescribeCodeCoverages</code>. This specifies the next item to return. To return the beginning of the list, exclude this parameter.</p>"""
    max_results: NotRequired["aws_sdk_codebuild.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""
    sort_order: NotRequired["aws_sdk_codebuild.types.sort_order_type.SortOrderType"]
    """<p>Specifies if the results are sorted in ascending or descending order.</p>"""
    sort_by: NotRequired[
        "aws_sdk_codebuild.types.report_code_coverage_sort_by_type.ReportCodeCoverageSortByType"
    ]
    """<p>Specifies how the results are sorted. Possible values are:</p> <dl> <dt>FILE_PATH</dt> <dd> <p>The results are sorted by file path.</p> </dd> <dt>LINE_COVERAGE_PERCENTAGE</dt> <dd> <p>The results are sorted by the percentage of lines that are covered.</p> </dd> </dl>"""
    min_line_coverage_percentage: NotRequired[
        "aws_sdk_codebuild.types.percentage.Percentage"
    ]
    """<p>The minimum line coverage percentage to report.</p>"""
    max_line_coverage_percentage: NotRequired[
        "aws_sdk_codebuild.types.percentage.Percentage"
    ]
    """<p>The maximum line coverage percentage to report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCodeCoveragesInput) -> dict:
    out: dict = {}
    out["reportArn"] = value["report_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "sort_order" in value:
        import aws_sdk_codebuild.types.sort_order_type

        out["sortOrder"] = (
            aws_sdk_codebuild.types.sort_order_type.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_codebuild.types.report_code_coverage_sort_by_type

        out["sortBy"] = (
            aws_sdk_codebuild.types.report_code_coverage_sort_by_type.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "min_line_coverage_percentage" in value:
        out["minLineCoveragePercentage"] = value["min_line_coverage_percentage"]
    if "max_line_coverage_percentage" in value:
        out["maxLineCoveragePercentage"] = value["max_line_coverage_percentage"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCodeCoveragesInput:
    out: DescribeCodeCoveragesInput = {}  # type: ignore[typeddict-item]
    if "reportArn" in data:
        out["report_arn"] = data["reportArn"]
    else:
        raise DeserializationError("DescribeCodeCoveragesInput.report_arn required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "sortOrder" in data:
        import aws_sdk_codebuild.types.sort_order_type

        out["sort_order"] = (
            aws_sdk_codebuild.types.sort_order_type.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if "sortBy" in data:
        import aws_sdk_codebuild.types.report_code_coverage_sort_by_type

        out["sort_by"] = (
            aws_sdk_codebuild.types.report_code_coverage_sort_by_type.deserialize_aws_json_1_1(
                data["sortBy"]
            )
        )
    if "minLineCoveragePercentage" in data:
        out["min_line_coverage_percentage"] = data["minLineCoveragePercentage"]
    if "maxLineCoveragePercentage" in data:
        out["max_line_coverage_percentage"] = data["maxLineCoveragePercentage"]
    return out
