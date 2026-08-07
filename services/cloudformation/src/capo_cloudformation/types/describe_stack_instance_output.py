"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackInstanceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stack_instance


class DescribeStackInstanceOutput(TypedDict, closed=True):
    stack_instance: NotRequired[
        "capo_cloudformation.types.stack_instance.StackInstance"
    ]
    """<p>The stack instance that matches the specified request parameters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackInstanceOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_instance" in value:
        import capo_cloudformation.types.stack_instance

        capo_cloudformation.types.stack_instance.serialize_query(
            value["stack_instance"], pairs, f"{key_prefix}StackInstance"
        )


def deserialize_query(el: Element) -> DescribeStackInstanceOutput:
    out: DescribeStackInstanceOutput = {}  # type: ignore[typeddict-item]
    child_stack_instance = el.find("StackInstance")
    if child_stack_instance is not None:
        import capo_cloudformation.types.stack_instance

        out["stack_instance"] = (
            capo_cloudformation.types.stack_instance.deserialize_query(
                child_stack_instance
            )
        )
    return out
