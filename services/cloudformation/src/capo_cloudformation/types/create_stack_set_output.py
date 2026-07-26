"""Generated from Smithy shape ``com.amazonaws.cloudformation#CreateStackSetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stack_set_id


class CreateStackSetOutput(TypedDict, closed=True):
    stack_set_id: NotRequired["capo_cloudformation.types.stack_set_id.StackSetId"]
    """<p>The ID of the StackSet that you're creating.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateStackSetOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_set_id" in value:
        pairs.append((f"{prefix}.StackSetId", str(value["stack_set_id"])))


def deserialize_query(el: Element) -> CreateStackSetOutput:
    out: CreateStackSetOutput = {}  # type: ignore[typeddict-item]
    child_stack_set_id = el.find("StackSetId")
    if child_stack_set_id is not None:
        out["stack_set_id"] = str(child_stack_set_id.text or "")
    return out
