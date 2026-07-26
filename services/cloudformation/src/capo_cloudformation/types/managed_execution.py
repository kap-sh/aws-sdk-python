"""Generated from Smithy shape ``com.amazonaws.cloudformation#ManagedExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.managed_execution_nullable


class ManagedExecution(TypedDict, closed=True):
    active: NotRequired[
        "capo_cloudformation.types.managed_execution_nullable.ManagedExecutionNullable"
    ]
    """<p>When <code>true</code>, CloudFormation performs non-conflicting operations concurrently and queues conflicting operations. After conflicting operations finish, CloudFormation starts queued operations in request order.</p> <note> <p>If there are already running or queued operations, CloudFormation queues all incoming operations even if they are non-conflicting.</p> <p>You can't modify your StackSet's execution configuration while there are running or queued operations for that StackSet.</p> </note> <p>When <code>false</code> (default), StackSets performs one operation at a time in request order.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ManagedExecution, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "active" in value:
        pairs.append((f"{prefix}.Active", "true" if value["active"] else "false"))


def deserialize_query(el: Element) -> ManagedExecution:
    out: ManagedExecution = {}  # type: ignore[typeddict-item]
    child_active = el.find("Active")
    if child_active is not None:
        out["active"] = (child_active.text or "").lower() == "true"
    return out
