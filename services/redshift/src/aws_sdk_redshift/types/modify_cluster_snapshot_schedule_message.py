"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyClusterSnapshotScheduleMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean_optional
    import aws_sdk_redshift.types.string


class ModifyClusterSnapshotScheduleMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A unique identifier for the cluster whose snapshot schedule you want to modify. </p>"""
    schedule_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A unique alphanumeric identifier for the schedule that you want to associate with the cluster.</p>"""
    disassociate_schedule: NotRequired[
        "aws_sdk_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>A boolean to indicate whether to remove the assoiciation between the cluster and the schedule.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyClusterSnapshotScheduleMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "schedule_identifier" in value:
        pairs.append(
            (f"{prefix}.ScheduleIdentifier", str(value["schedule_identifier"]))
        )
    if "disassociate_schedule" in value:
        pairs.append(
            (
                f"{prefix}.DisassociateSchedule",
                "true" if value["disassociate_schedule"] else "false",
            )
        )


def deserialize_query(el: Element) -> ModifyClusterSnapshotScheduleMessage:
    out: ModifyClusterSnapshotScheduleMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_schedule_identifier = el.find("ScheduleIdentifier")
    if child_schedule_identifier is not None:
        out["schedule_identifier"] = str(child_schedule_identifier.text or "")
    child_disassociate_schedule = el.find("DisassociateSchedule")
    if child_disassociate_schedule is not None:
        out["disassociate_schedule"] = (
            child_disassociate_schedule.text or ""
        ).lower() == "true"
    return out
