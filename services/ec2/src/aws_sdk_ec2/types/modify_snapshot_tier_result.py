"""Generated from Smithy shape ``com.amazonaws.ec2#ModifySnapshotTierResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class ModifySnapshotTierResult(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    tiering_start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the archive process was started.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifySnapshotTierResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "tiering_start_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["tiering_start_time"], pairs, f"{prefix}.TieringStartTime"
        )


def deserialize_ec2_query(el: Element) -> ModifySnapshotTierResult:
    out: ModifySnapshotTierResult = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_tiering_start_time = el.find("TieringStartTime")
    if child_tiering_start_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["tiering_start_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_tiering_start_time
            )
        )
    return out
