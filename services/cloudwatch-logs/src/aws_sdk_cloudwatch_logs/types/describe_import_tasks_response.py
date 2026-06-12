"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeImportTasksResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.import_list
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeImportTasksResponse(TypedDict):
    imports: NotRequired["aws_sdk_cloudwatch_logs.types.import_list.ImportList"]
    """<p>The list of import tasks that match the request filters.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of results. Not present if there are no additional results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImportTasksResponse) -> dict:
    out: dict = {}
    if "imports" in value:
        import aws_sdk_cloudwatch_logs.types.import_list

        out["imports"] = (
            aws_sdk_cloudwatch_logs.types.import_list.serialize_aws_json_1_1(
                value["imports"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImportTasksResponse:
    out: DescribeImportTasksResponse = {}  # type: ignore[typeddict-item]
    if "imports" in data:
        import aws_sdk_cloudwatch_logs.types.import_list

        out["imports"] = (
            aws_sdk_cloudwatch_logs.types.import_list.deserialize_aws_json_1_1(
                data["imports"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
