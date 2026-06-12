"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#ListHumanLoopsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_a2i_runtime.types.flow_definition_arn
    import aws_sdk_sagemaker_a2i_runtime.types.max_results
    import aws_sdk_sagemaker_a2i_runtime.types.next_token
    import aws_sdk_sagemaker_a2i_runtime.types.sort_order
    import aws_sdk_sagemaker_a2i_runtime.types.timestamp


class ListHumanLoopsRequest(TypedDict):
    creation_time_after: NotRequired[
        "aws_sdk_sagemaker_a2i_runtime.types.timestamp.Timestamp"
    ]
    """<p>(Optional) The timestamp of the date when you want the human loops to begin in ISO 8601 format. For example, <code>2020-02-24</code>.</p>"""
    creation_time_before: NotRequired[
        "aws_sdk_sagemaker_a2i_runtime.types.timestamp.Timestamp"
    ]
    """<p>(Optional) The timestamp of the date before which you want the human loops to begin in ISO 8601 format. For example, <code>2020-02-24</code>.</p>"""
    flow_definition_arn: NotRequired[
        "aws_sdk_sagemaker_a2i_runtime.types.flow_definition_arn.FlowDefinitionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a flow definition.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker_a2i_runtime.types.sort_order.SortOrder"]
    """<p>Optional. The order for displaying results. Valid values: <code>Ascending</code> and <code>Descending</code>.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker_a2i_runtime.types.next_token.NextToken"]
    """<p>A token to display the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_sagemaker_a2i_runtime.types.max_results.MaxResults"
    ]
    """<p>The total number of items to return. If the total number of available items is more than the value specified in <code>MaxResults</code>, then a <code>NextToken</code> is returned in the output. You can use this token to display the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHumanLoopsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListHumanLoopsRequest:
    out: ListHumanLoopsRequest = {}  # type: ignore[typeddict-item]
    return out
