"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteScheduledActionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class DeleteScheduledActionMessage(TypedDict):
    scheduled_action_name: NotRequired["aws_sdk_redshift.types.string.String"]
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
