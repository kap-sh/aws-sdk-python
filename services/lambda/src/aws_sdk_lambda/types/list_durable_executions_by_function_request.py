"""Generated from Smithy shape ``com.amazonaws.lambda#ListDurableExecutionsByFunctionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.durable_execution_name
    import aws_sdk_lambda.types.execution_status_list
    import aws_sdk_lambda.types.execution_timestamp
    import aws_sdk_lambda.types.item_count
    import aws_sdk_lambda.types.namespaced_function_name
    import aws_sdk_lambda.types.numeric_latest_published_or_alias_qualifier
    import aws_sdk_lambda.types.reverse_order
    import aws_sdk_lambda.types.string


class ListDurableExecutionsByFunctionRequest(TypedDict):
    function_name: (
        "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName"
    )
    """<p>The name or ARN of the Lambda function. You can specify a function name, a partial ARN, or a full ARN.</p>"""
    qualifier: NotRequired[
        "aws_sdk_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
    ]
    """<p>The function version or alias. If not specified, lists executions for the $LATEST version.</p>"""
    durable_execution_name: NotRequired[
        "aws_sdk_lambda.types.durable_execution_name.DurableExecutionName"
    ]
    """<p>Filter executions by name. Only executions with names that matches this string are returned.</p>"""
    statuses: NotRequired[
        "aws_sdk_lambda.types.execution_status_list.ExecutionStatusList"
    ]
    """<p>Filter executions by status. Valid values: RUNNING, SUCCEEDED, FAILED, TIMED_OUT, STOPPED.</p>"""
    started_after: NotRequired[
        "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
    ]
    """<p>Filter executions that started after this timestamp (ISO 8601 format).</p>"""
    started_before: NotRequired[
        "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
    ]
    """<p>Filter executions that started before this timestamp (ISO 8601 format).</p>"""
    reverse_order: NotRequired["aws_sdk_lambda.types.reverse_order.ReverseOrder"]
    """<p>Set to true to return results in reverse chronological order (newest first). Default is false.</p>"""
    marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>Pagination token from a previous request to continue retrieving results.</p>"""
    max_items: "aws_sdk_lambda.types.item_count.ItemCount"
    """<p>Maximum number of executions to return (1-1000). Default is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDurableExecutionsByFunctionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDurableExecutionsByFunctionRequest:
    out: ListDurableExecutionsByFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
