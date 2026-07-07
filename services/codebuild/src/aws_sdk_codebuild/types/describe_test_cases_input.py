"""Generated from Smithy shape ``com.amazonaws.codebuild#DescribeTestCasesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.page_size
    import aws_sdk_codebuild.types.string
    import aws_sdk_codebuild.types.test_case_filter


class DescribeTestCasesInput(TypedDict, closed=True):
    report_arn: "aws_sdk_codebuild.types.string.String"
    """<p> The ARN of the report for which test cases are returned. </p>"""
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>"""
    max_results: NotRequired["aws_sdk_codebuild.types.page_size.PageSize"]
    """<p> The maximum number of paginated test cases returned per response. Use <code>nextToken</code> to iterate pages in the list of returned <code>TestCase</code> objects. The default value is 100. </p>"""
    filter: NotRequired["aws_sdk_codebuild.types.test_case_filter.TestCaseFilter"]
    """<p> A <code>TestCaseFilter</code> object used to filter the returned reports. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTestCasesInput) -> dict:
    out: dict = {}
    out["reportArn"] = value["report_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter" in value:
        import aws_sdk_codebuild.types.test_case_filter

        out["filter"] = aws_sdk_codebuild.types.test_case_filter.serialize_aws_json_1_1(
            value["filter"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTestCasesInput:
    out: DescribeTestCasesInput = {}  # type: ignore[typeddict-item]
    if "reportArn" in data:
        out["report_arn"] = data["reportArn"]
    else:
        raise DeserializationError("DescribeTestCasesInput.report_arn required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filter" in data:
        import aws_sdk_codebuild.types.test_case_filter

        out["filter"] = (
            aws_sdk_codebuild.types.test_case_filter.deserialize_aws_json_1_1(
                data["filter"]
            )
        )
    return out
