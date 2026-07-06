"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeSnapshotSchedulesOutputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.snapshot_schedule_list
    import aws_sdk_redshift.types.string


class DescribeSnapshotSchedulesOutputMessage(TypedDict, closed=True):
    snapshot_schedules: NotRequired[
        "aws_sdk_redshift.types.snapshot_schedule_list.SnapshotScheduleList"
    ]
    """<p>A list of SnapshotSchedules.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>marker</code> parameter and retrying the command. If the <code>marker</code> field is empty, all response records have been retrieved for the request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeSnapshotSchedulesOutputMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "snapshot_schedules" in value:
        import aws_sdk_redshift.types.snapshot_schedule_list

        aws_sdk_redshift.types.snapshot_schedule_list.serialize_query(
            value["snapshot_schedules"], pairs, f"{prefix}.SnapshotSchedules"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeSnapshotSchedulesOutputMessage:
    out: DescribeSnapshotSchedulesOutputMessage = {}  # type: ignore[typeddict-item]
    child_snapshot_schedules = el.find("SnapshotSchedules")
    if child_snapshot_schedules is not None:
        import aws_sdk_redshift.types.snapshot_schedule_list

        out["snapshot_schedules"] = (
            aws_sdk_redshift.types.snapshot_schedule_list.deserialize_query(
                child_snapshot_schedules
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
