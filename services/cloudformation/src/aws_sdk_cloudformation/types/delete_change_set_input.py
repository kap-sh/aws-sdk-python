"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeleteChangeSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.change_set_name_or_id
    import aws_sdk_cloudformation.types.stack_name_or_id


class DeleteChangeSetInput(TypedDict, closed=True):
    change_set_name: NotRequired[
        "aws_sdk_cloudformation.types.change_set_name_or_id.ChangeSetNameOrId"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the change set that you want to delete.</p>"""
    stack_name: NotRequired[
        "aws_sdk_cloudformation.types.stack_name_or_id.StackNameOrId"
    ]
    """<p>If you specified the name of a change set to delete, specify the stack name or Amazon Resource Name (ARN) that's associated with it.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteChangeSetInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "change_set_name" in value:
        pairs.append((f"{prefix}.ChangeSetName", str(value["change_set_name"])))
    if "stack_name" in value:
        pairs.append((f"{prefix}.StackName", str(value["stack_name"])))


def deserialize_query(el: Element) -> DeleteChangeSetInput:
    out: DeleteChangeSetInput = {}  # type: ignore[typeddict-item]
    child_change_set_name = el.find("ChangeSetName")
    if child_change_set_name is not None:
        out["change_set_name"] = str(child_change_set_name.text or "")
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    return out
