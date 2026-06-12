"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackRefactorInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_refactor_id


class DescribeStackRefactorInput(TypedDict):
    stack_refactor_id: NotRequired[
        "aws_sdk_cloudformation.types.stack_refactor_id.StackRefactorId"
    ]
    """<p>The ID associated with the stack refactor created from the <a>CreateStackRefactor</a> action.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackRefactorInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_refactor_id" in value:
        pairs.append((f"{prefix}.StackRefactorId", str(value["stack_refactor_id"])))


def deserialize_query(el: Element) -> DescribeStackRefactorInput:
    out: DescribeStackRefactorInput = {}  # type: ignore[typeddict-item]
    child_stack_refactor_id = el.find("StackRefactorId")
    if child_stack_refactor_id is not None:
        out["stack_refactor_id"] = str(child_stack_refactor_id.text or "")
    return out
