"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastSnapshotRestoreStateErrorItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_fast_snapshot_restore_state_error
    import aws_sdk_ec2.types.string


class EnableFastSnapshotRestoreStateErrorItem(TypedDict, closed=True):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
    error: NotRequired[
        "aws_sdk_ec2.types.enable_fast_snapshot_restore_state_error.EnableFastSnapshotRestoreStateError"
    ]
    """<p>The error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableFastSnapshotRestoreStateErrorItem,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "error" in value:
        import aws_sdk_ec2.types.enable_fast_snapshot_restore_state_error

        aws_sdk_ec2.types.enable_fast_snapshot_restore_state_error.serialize_ec2_query(
            value["error"], pairs, f"{prefix}.Error"
        )


def deserialize_ec2_query(el: Element) -> EnableFastSnapshotRestoreStateErrorItem:
    out: EnableFastSnapshotRestoreStateErrorItem = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_error = el.find("Error")
    if child_error is not None:
        import aws_sdk_ec2.types.enable_fast_snapshot_restore_state_error

        out["error"] = (
            aws_sdk_ec2.types.enable_fast_snapshot_restore_state_error.deserialize_ec2_query(
                child_error
            )
        )
    return out
