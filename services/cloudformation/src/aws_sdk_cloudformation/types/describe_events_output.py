"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeEventsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.operation_events


class DescribeEventsOutput(TypedDict, closed=True):
    operation_events: NotRequired[
        "aws_sdk_cloudformation.types.operation_events.OperationEvents"
    ]
    """<p>A list of operation events that match the specified criteria.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <code>DescribeEvents</code> again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to <code>null</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEventsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "operation_events" in value:
        import aws_sdk_cloudformation.types.operation_events

        aws_sdk_cloudformation.types.operation_events.serialize_query(
            value["operation_events"], pairs, f"{prefix}.OperationEvents"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeEventsOutput:
    out: DescribeEventsOutput = {}  # type: ignore[typeddict-item]
    child_operation_events = el.find("OperationEvents")
    if child_operation_events is not None:
        import aws_sdk_cloudformation.types.operation_events

        out["operation_events"] = (
            aws_sdk_cloudformation.types.operation_events.deserialize_query(
                child_operation_events
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
