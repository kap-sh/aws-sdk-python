"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeEventsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.change_set_name_or_id
    import aws_sdk_cloudformation.types.event_filter
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.operation_id
    import aws_sdk_cloudformation.types.stack_name_or_id


class DescribeEventsInput(TypedDict, closed=True):
    stack_name: NotRequired[
        "aws_sdk_cloudformation.types.stack_name_or_id.StackNameOrId"
    ]
    """<p>The name or unique stack ID for which you want to retrieve events.</p>"""
    change_set_name: NotRequired[
        "aws_sdk_cloudformation.types.change_set_name_or_id.ChangeSetNameOrId"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the change set for which you want to retrieve events.</p>"""
    operation_id: NotRequired["aws_sdk_cloudformation.types.operation_id.OperationId"]
    """<p>The unique identifier of the operation for which you want to retrieve events.</p>"""
    filters: NotRequired["aws_sdk_cloudformation.types.event_filter.EventFilter"]
    """<p>Filters to apply when retrieving events.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEventsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))
    if "change_set_name" in value:
        pairs.append((f"{prefix}.ChangeSetName", str(value["change_set_name"])))
    if "operation_id" in value:
        pairs.append((f"{prefix}.OperationId", str(value["operation_id"])))
    if "filters" in value:
        import aws_sdk_cloudformation.types.event_filter

        aws_sdk_cloudformation.types.event_filter.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeEventsInput:
    out: DescribeEventsInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_change_set_name = el.find("ChangeSetName")
    if child_change_set_name is not None:
        out["change_set_name"] = str(child_change_set_name.text or "")
    child_operation_id = el.find("OperationId")
    if child_operation_id is not None:
        out["operation_id"] = str(child_operation_id.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_cloudformation.types.event_filter

        out["filters"] = aws_sdk_cloudformation.types.event_filter.deserialize_query(
            child_filters
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
