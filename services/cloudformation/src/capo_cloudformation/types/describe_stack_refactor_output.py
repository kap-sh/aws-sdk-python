"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackRefactorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.description
    import capo_cloudformation.types.execution_status_reason
    import capo_cloudformation.types.stack_ids
    import capo_cloudformation.types.stack_refactor_execution_status
    import capo_cloudformation.types.stack_refactor_id
    import capo_cloudformation.types.stack_refactor_status
    import capo_cloudformation.types.stack_refactor_status_reason


class DescribeStackRefactorOutput(TypedDict, closed=True):
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>A description to help you identify the refactor.</p>"""
    stack_refactor_id: NotRequired[
        "capo_cloudformation.types.stack_refactor_id.StackRefactorId"
    ]
    """<p>The ID associated with the stack refactor created from the <a>CreateStackRefactor</a> action.</p>"""
    stack_ids: NotRequired["capo_cloudformation.types.stack_ids.StackIds"]
    """<p>The unique ID for each stack.</p>"""
    execution_status: NotRequired[
        "capo_cloudformation.types.stack_refactor_execution_status.StackRefactorExecutionStatus"
    ]
    """<p>The stack refactor execution operation status that's provided after calling the <a>ExecuteStackRefactor</a> action.</p>"""
    execution_status_reason: NotRequired[
        "capo_cloudformation.types.execution_status_reason.ExecutionStatusReason"
    ]
    """<p>A detailed explanation for the stack refactor <code>ExecutionStatus</code>.</p>"""
    status: NotRequired[
        "capo_cloudformation.types.stack_refactor_status.StackRefactorStatus"
    ]
    """<p>The stack refactor operation status that's provided after calling the <a>CreateStackRefactor</a> action.</p>"""
    status_reason: NotRequired[
        "capo_cloudformation.types.stack_refactor_status_reason.StackRefactorStatusReason"
    ]
    """<p>A detailed explanation for the stack refactor operation <code>Status</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackRefactorOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "stack_refactor_id" in value:
        pairs.append((f"{key_prefix}StackRefactorId", str(value["stack_refactor_id"])))
    if "stack_ids" in value:
        import capo_cloudformation.types.stack_ids

        capo_cloudformation.types.stack_ids.serialize_query(
            value["stack_ids"], pairs, f"{key_prefix}StackIds"
        )
    if "execution_status" in value:
        import capo_cloudformation.types.stack_refactor_execution_status

        capo_cloudformation.types.stack_refactor_execution_status.serialize_query(
            value["execution_status"], pairs, f"{key_prefix}ExecutionStatus"
        )
    if "execution_status_reason" in value:
        pairs.append(
            (
                f"{key_prefix}ExecutionStatusReason",
                str(value["execution_status_reason"]),
            )
        )
    if "status" in value:
        import capo_cloudformation.types.stack_refactor_status

        capo_cloudformation.types.stack_refactor_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "status_reason" in value:
        pairs.append((f"{key_prefix}StatusReason", str(value["status_reason"])))


def deserialize_query(el: Element) -> DescribeStackRefactorOutput:
    out: DescribeStackRefactorOutput = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_stack_refactor_id = el.find("StackRefactorId")
    if child_stack_refactor_id is not None:
        out["stack_refactor_id"] = str(child_stack_refactor_id.text or "")
    child_stack_ids = el.find("StackIds")
    if child_stack_ids is not None:
        import capo_cloudformation.types.stack_ids

        out["stack_ids"] = capo_cloudformation.types.stack_ids.deserialize_query(
            child_stack_ids
        )
    child_execution_status = el.find("ExecutionStatus")
    if child_execution_status is not None:
        import capo_cloudformation.types.stack_refactor_execution_status

        out["execution_status"] = (
            capo_cloudformation.types.stack_refactor_execution_status.deserialize_query(
                child_execution_status
            )
        )
    child_execution_status_reason = el.find("ExecutionStatusReason")
    if child_execution_status_reason is not None:
        out["execution_status_reason"] = str(child_execution_status_reason.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.stack_refactor_status

        out["status"] = (
            capo_cloudformation.types.stack_refactor_status.deserialize_query(
                child_status
            )
        )
    child_status_reason = el.find("StatusReason")
    if child_status_reason is not None:
        out["status_reason"] = str(child_status_reason.text or "")
    return out
