"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteSnapshotScheduleMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class DeleteSnapshotScheduleMessage(TypedDict, closed=True):
    schedule_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>A unique identifier of the snapshot schedule to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSnapshotScheduleMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "schedule_identifier" in value:
        pairs.append(
            (f"{prefix}.ScheduleIdentifier", str(value["schedule_identifier"]))
        )


def deserialize_query(el: Element) -> DeleteSnapshotScheduleMessage:
    out: DeleteSnapshotScheduleMessage = {}  # type: ignore[typeddict-item]
    child_schedule_identifier = el.find("ScheduleIdentifier")
    if child_schedule_identifier is not None:
        out["schedule_identifier"] = str(child_schedule_identifier.text or "")
    return out
