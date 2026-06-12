"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeChangeSetHooksOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.change_set_hooks
    import aws_sdk_cloudformation.types.change_set_hooks_status
    import aws_sdk_cloudformation.types.change_set_id
    import aws_sdk_cloudformation.types.change_set_name
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.stack_id
    import aws_sdk_cloudformation.types.stack_name


class DescribeChangeSetHooksOutput(TypedDict):
    change_set_id: NotRequired["aws_sdk_cloudformation.types.change_set_id.ChangeSetId"]
    """<p>The change set identifier (stack ID).</p>"""
    change_set_name: NotRequired[
        "aws_sdk_cloudformation.types.change_set_name.ChangeSetName"
    ]
    """<p>The change set name.</p>"""
    hooks: NotRequired["aws_sdk_cloudformation.types.change_set_hooks.ChangeSetHooks"]
    """<p>List of Hook objects.</p>"""
    status: NotRequired[
        "aws_sdk_cloudformation.types.change_set_hooks_status.ChangeSetHooksStatus"
    ]
    """<p>Provides the status of the change set Hook.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>Pagination token, <code>null</code> or empty if no more results.</p>"""
    stack_id: NotRequired["aws_sdk_cloudformation.types.stack_id.StackId"]
    """<p>The stack identifier (stack ID).</p>"""
    stack_name: NotRequired["aws_sdk_cloudformation.types.stack_name.StackName"]
    """<p>The stack name.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeChangeSetHooksOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "change_set_id" in value:
        pairs.append((f"{prefix}.ChangeSetId", str(value["change_set_id"])))
    if "change_set_name" in value:
        pairs.append((f"{prefix}.ChangeSetName", str(value["change_set_name"])))
    if "hooks" in value:
        import aws_sdk_cloudformation.types.change_set_hooks

        aws_sdk_cloudformation.types.change_set_hooks.serialize_query(
            value["hooks"], pairs, f"{prefix}.Hooks"
        )
    if "status" in value:
        import aws_sdk_cloudformation.types.change_set_hooks_status

        aws_sdk_cloudformation.types.change_set_hooks_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "stack_id" in value:
        pairs.append((f"{prefix}.StackId", str(value["stack_id"])))
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))


def deserialize_query(el: Element) -> DescribeChangeSetHooksOutput:
    out: DescribeChangeSetHooksOutput = {}  # type: ignore[typeddict-item]
    child_change_set_id = el.find("ChangeSetId")
    if child_change_set_id is not None:
        out["change_set_id"] = str(child_change_set_id.text or "")
    child_change_set_name = el.find("ChangeSetName")
    if child_change_set_name is not None:
        out["change_set_name"] = str(child_change_set_name.text or "")
    child_hooks = el.find("Hooks")
    if child_hooks is not None:
        import aws_sdk_cloudformation.types.change_set_hooks

        out["hooks"] = aws_sdk_cloudformation.types.change_set_hooks.deserialize_query(
            child_hooks
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_cloudformation.types.change_set_hooks_status

        out["status"] = (
            aws_sdk_cloudformation.types.change_set_hooks_status.deserialize_query(
                child_status
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    return out
