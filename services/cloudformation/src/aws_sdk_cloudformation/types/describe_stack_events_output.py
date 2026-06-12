"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackEventsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.stack_events


class DescribeStackEventsOutput(TypedDict):
    stack_events: NotRequired["aws_sdk_cloudformation.types.stack_events.StackEvents"]
    """<p>A list of <code>StackEvents</code> structures.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>If the output exceeds 1 MB in size, a string that identifies the next page of events. If no additional page exists, this value is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackEventsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_events" in value:
        import aws_sdk_cloudformation.types.stack_events

        aws_sdk_cloudformation.types.stack_events.serialize_query(
            value["stack_events"], pairs, f"{prefix}.StackEvents"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeStackEventsOutput:
    out: DescribeStackEventsOutput = {}  # type: ignore[typeddict-item]
    child_stack_events = el.find("StackEvents")
    if child_stack_events is not None:
        import aws_sdk_cloudformation.types.stack_events

        out["stack_events"] = (
            aws_sdk_cloudformation.types.stack_events.deserialize_query(
                child_stack_events
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
