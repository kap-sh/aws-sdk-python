"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterAssociatedToSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.schedule_state
    import aws_sdk_redshift.types.string


class ClusterAssociatedToSchedule(TypedDict, closed=True):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p></p>"""
    schedule_association_state: NotRequired[
        "aws_sdk_redshift.types.schedule_state.ScheduleState"
    ]
    """<p></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterAssociatedToSchedule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "schedule_association_state" in value:
        import aws_sdk_redshift.types.schedule_state

        aws_sdk_redshift.types.schedule_state.serialize_query(
            value["schedule_association_state"],
            pairs,
            f"{prefix}.ScheduleAssociationState",
        )


def deserialize_query(el: Element) -> ClusterAssociatedToSchedule:
    out: ClusterAssociatedToSchedule = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_schedule_association_state = el.find("ScheduleAssociationState")
    if child_schedule_association_state is not None:
        import aws_sdk_redshift.types.schedule_state

        out["schedule_association_state"] = (
            aws_sdk_redshift.types.schedule_state.deserialize_query(
                child_schedule_association_state
            )
        )
    return out
