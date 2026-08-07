"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackInstanceComprehensiveStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stack_instance_detailed_status


class StackInstanceComprehensiveStatus(TypedDict, closed=True):
    detailed_status: NotRequired[
        "capo_cloudformation.types.stack_instance_detailed_status.StackInstanceDetailedStatus"
    ]
    """<ul> <li> <p> <code>CANCELLED</code>: The operation in the specified account and Region has been canceled. This is either because a user has stopped the StackSet operation, or because the failure tolerance of the StackSet operation has been exceeded.</p> </li> <li> <p> <code>FAILED</code>: The operation in the specified account and Region failed. If the StackSet operation fails in enough accounts within a Region, the failure tolerance for the StackSet operation as a whole might be exceeded.</p> </li> <li> <p> <code>FAILED_IMPORT</code>: The import of the stack instance in the specified account and Region failed and left the stack in an unstable state. Once the issues causing the failure are fixed, the import operation can be retried. If enough StackSet operations fail in enough accounts within a Region, the failure tolerance for the StackSet operation as a whole might be exceeded.</p> </li> <li> <p> <code>INOPERABLE</code>: A <code>DeleteStackInstances</code> operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further <code>UpdateStackSet</code> operations. You might need to perform a <code>DeleteStackInstances</code> operation, with <code>RetainStacks</code> set to <code>true</code>, to delete the stack instance, and then delete the stack manually.</p> </li> <li> <p> <code>PENDING</code>: The operation in the specified account and Region has yet to start.</p> </li> <li> <p> <code>RUNNING</code>: The operation in the specified account and Region is currently in progress.</p> </li> <li> <p> <code>SKIPPED_SUSPENDED_ACCOUNT</code>: The operation in the specified account and Region has been skipped because the account was suspended at the time of the operation.</p> </li> <li> <p> <code>SUCCEEDED</code>: The operation in the specified account and Region completed successfully.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackInstanceComprehensiveStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "detailed_status" in value:
        import capo_cloudformation.types.stack_instance_detailed_status

        capo_cloudformation.types.stack_instance_detailed_status.serialize_query(
            value["detailed_status"], pairs, f"{key_prefix}DetailedStatus"
        )


def deserialize_query(el: Element) -> StackInstanceComprehensiveStatus:
    out: StackInstanceComprehensiveStatus = {}  # type: ignore[typeddict-item]
    child_detailed_status = el.find("DetailedStatus")
    if child_detailed_status is not None:
        import capo_cloudformation.types.stack_instance_detailed_status

        out["detailed_status"] = (
            capo_cloudformation.types.stack_instance_detailed_status.deserialize_query(
                child_detailed_status
            )
        )
    return out
