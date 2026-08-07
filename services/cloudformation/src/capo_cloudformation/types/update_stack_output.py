"""Generated from Smithy shape ``com.amazonaws.cloudformation#UpdateStackOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.operation_id
    import capo_cloudformation.types.stack_id


class UpdateStackOutput(TypedDict, closed=True):
    stack_id: NotRequired["capo_cloudformation.types.stack_id.StackId"]
    """<p>Unique identifier of the stack.</p>"""
    operation_id: NotRequired["capo_cloudformation.types.operation_id.OperationId"]
    """<p>A unique identifier for this update operation that can be used to track the operation's progress and events.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateStackOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_id" in value:
        pairs.append((f"{key_prefix}StackId", str(value["stack_id"])))
    if "operation_id" in value:
        pairs.append((f"{key_prefix}OperationId", str(value["operation_id"])))


def deserialize_query(el: Element) -> UpdateStackOutput:
    out: UpdateStackOutput = {}  # type: ignore[typeddict-item]
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
    child_operation_id = el.find("OperationId")
    if child_operation_id is not None:
        out["operation_id"] = str(child_operation_id.text or "")
    return out
