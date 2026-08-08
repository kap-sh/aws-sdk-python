"""Generated from Smithy shape ``com.amazonaws.ec2#CancelImportTaskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class CancelImportTaskResult(TypedDict, closed=True):
    import_task_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the task being canceled.</p>"""
    previous_state: NotRequired["capo_ec2.types.string.String"]
    """<p>The current state of the task being canceled.</p>"""
    state: NotRequired["capo_ec2.types.string.String"]
    """<p>The current state of the task being canceled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelImportTaskResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "import_task_id" in value:
        pairs.append((f"{key_prefix}ImportTaskId", str(value["import_task_id"])))
    if "previous_state" in value:
        pairs.append((f"{key_prefix}PreviousState", str(value["previous_state"])))
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))


def deserialize_ec2_query(el: Element) -> CancelImportTaskResult:
    out: CancelImportTaskResult = {}  # type: ignore[typeddict-item]
    child_import_task_id = el.find("importTaskId")
    if child_import_task_id is not None:
        out["import_task_id"] = str(child_import_task_id.text or "")
    child_previous_state = el.find("previousState")
    if child_previous_state is not None:
        out["previous_state"] = str(child_previous_state.text or "")
    child_state = el.find("state")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    return out
