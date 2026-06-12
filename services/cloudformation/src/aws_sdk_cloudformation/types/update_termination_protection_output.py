"""Generated from Smithy shape ``com.amazonaws.cloudformation#UpdateTerminationProtectionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_id


class UpdateTerminationProtectionOutput(TypedDict):
    stack_id: NotRequired["aws_sdk_cloudformation.types.stack_id.StackId"]
    """<p>The unique ID of the stack.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateTerminationProtectionOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_id" in value:
        pairs.append((f"{prefix}.StackId", str(value["stack_id"])))


def deserialize_query(el: Element) -> UpdateTerminationProtectionOutput:
    out: UpdateTerminationProtectionOutput = {}  # type: ignore[typeddict-item]
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
    return out
