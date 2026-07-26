"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteScheduledActionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class DeleteScheduledActionMessage(TypedDict, closed=True):
    scheduled_action_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the scheduled action to delete. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteScheduledActionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "scheduled_action_name" in value:
        pairs.append(
            (f"{prefix}.ScheduledActionName", str(value["scheduled_action_name"]))
        )


def deserialize_query(el: Element) -> DeleteScheduledActionMessage:
    out: DeleteScheduledActionMessage = {}  # type: ignore[typeddict-item]
    child_scheduled_action_name = el.find("ScheduledActionName")
    if child_scheduled_action_name is not None:
        out["scheduled_action_name"] = str(child_scheduled_action_name.text or "")
    return out
