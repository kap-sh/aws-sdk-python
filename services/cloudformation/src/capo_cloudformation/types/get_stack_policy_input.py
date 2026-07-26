"""Generated from Smithy shape ``com.amazonaws.cloudformation#GetStackPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stack_name


class GetStackPolicyInput(TypedDict, closed=True):
    stack_name: NotRequired["capo_cloudformation.types.stack_name.StackName"]
    """<p>The name or unique stack ID that's associated with the stack whose policy you want to get.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetStackPolicyInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))


def deserialize_query(el: Element) -> GetStackPolicyInput:
    out: GetStackPolicyInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    return out
