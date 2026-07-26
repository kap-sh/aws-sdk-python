"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetOperationStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.failed_stack_instances_count


class StackSetOperationStatusDetails(TypedDict, closed=True):
    failed_stack_instances_count: NotRequired[
        "capo_cloudformation.types.failed_stack_instances_count.FailedStackInstancesCount"
    ]
    """<p>The number of stack instances for which the StackSet operation failed.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackSetOperationStatusDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "failed_stack_instances_count" in value:
        pairs.append(
            (
                f"{prefix}.FailedStackInstancesCount",
                str(value["failed_stack_instances_count"]),
            )
        )


def deserialize_query(el: Element) -> StackSetOperationStatusDetails:
    out: StackSetOperationStatusDetails = {}  # type: ignore[typeddict-item]
    child_failed_stack_instances_count = el.find("FailedStackInstancesCount")
    if child_failed_stack_instances_count is not None:
        out["failed_stack_instances_count"] = int(
            child_failed_stack_instances_count.text or ""
        )
    return out
