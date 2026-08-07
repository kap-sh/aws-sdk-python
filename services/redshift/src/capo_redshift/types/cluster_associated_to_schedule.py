"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterAssociatedToSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.schedule_state
    import capo_redshift.types.string


class ClusterAssociatedToSchedule(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p></p>"""
    schedule_association_state: NotRequired[
        "capo_redshift.types.schedule_state.ScheduleState"
    ]
    """<p></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterAssociatedToSchedule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "schedule_association_state" in value:
        import capo_redshift.types.schedule_state

        capo_redshift.types.schedule_state.serialize_query(
            value["schedule_association_state"],
            pairs,
            f"{key_prefix}ScheduleAssociationState",
        )


def deserialize_query(el: Element) -> ClusterAssociatedToSchedule:
    out: ClusterAssociatedToSchedule = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_schedule_association_state = el.find("ScheduleAssociationState")
    if child_schedule_association_state is not None:
        import capo_redshift.types.schedule_state

        out["schedule_association_state"] = (
            capo_redshift.types.schedule_state.deserialize_query(
                child_schedule_association_state
            )
        )
    return out
