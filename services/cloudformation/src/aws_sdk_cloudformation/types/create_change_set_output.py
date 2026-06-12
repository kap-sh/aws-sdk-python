"""Generated from Smithy shape ``com.amazonaws.cloudformation#CreateChangeSetOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.change_set_id
    import aws_sdk_cloudformation.types.stack_id


class CreateChangeSetOutput(TypedDict):
    id: NotRequired["aws_sdk_cloudformation.types.change_set_id.ChangeSetId"]
    """<p>The Amazon Resource Name (ARN) of the change set.</p>"""
    stack_id: NotRequired["aws_sdk_cloudformation.types.stack_id.StackId"]
    """<p>The unique ID of the stack.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateChangeSetOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "id" in value:
        pairs.append((f"{prefix}.Id", str(value["id"])))
    if "stack_id" in value:
        pairs.append((f"{prefix}.StackId", str(value["stack_id"])))


def deserialize_query(el: Element) -> CreateChangeSetOutput:
    out: CreateChangeSetOutput = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
    return out
