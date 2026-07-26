"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeChangeSetHooksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.change_set_name_or_id
    import capo_cloudformation.types.logical_resource_id
    import capo_cloudformation.types.next_token
    import capo_cloudformation.types.stack_name_or_id


class DescribeChangeSetHooksInput(TypedDict, closed=True):
    change_set_name: NotRequired[
        "capo_cloudformation.types.change_set_name_or_id.ChangeSetNameOrId"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the change set that you want to describe.</p>"""
    stack_name: NotRequired["capo_cloudformation.types.stack_name_or_id.StackNameOrId"]
    """<p>If you specified the name of a change set, specify the stack name or stack ID (ARN) of the change set you want to describe.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    logical_resource_id: NotRequired[
        "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>If specified, lists only the Hooks related to the specified <code>LogicalResourceId</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeChangeSetHooksInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "change_set_name" in value:
        pairs.append((f"{prefix}.ChangeSetName", str(value["change_set_name"])))
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "logical_resource_id" in value:
        pairs.append((f"{prefix}.LogicalResourceId", str(value["logical_resource_id"])))


def deserialize_query(el: Element) -> DescribeChangeSetHooksInput:
    out: DescribeChangeSetHooksInput = {}  # type: ignore[typeddict-item]
    child_change_set_name = el.find("ChangeSetName")
    if child_change_set_name is not None:
        out["change_set_name"] = str(child_change_set_name.text or "")
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_logical_resource_id = el.find("LogicalResourceId")
    if child_logical_resource_id is not None:
        out["logical_resource_id"] = str(child_logical_resource_id.text or "")
    return out
