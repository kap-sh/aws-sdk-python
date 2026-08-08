"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastSnapshotRestoreStateErrorItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.disable_fast_snapshot_restore_state_error
    import capo_ec2.types.string


class DisableFastSnapshotRestoreStateErrorItem(TypedDict, closed=True):
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
    error: NotRequired[
        "capo_ec2.types.disable_fast_snapshot_restore_state_error.DisableFastSnapshotRestoreStateError"
    ]
    """<p>The error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableFastSnapshotRestoreStateErrorItem,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "error" in value:
        import capo_ec2.types.disable_fast_snapshot_restore_state_error

        capo_ec2.types.disable_fast_snapshot_restore_state_error.serialize_ec2_query(
            value["error"], pairs, f"{key_prefix}Error"
        )


def deserialize_ec2_query(el: Element) -> DisableFastSnapshotRestoreStateErrorItem:
    out: DisableFastSnapshotRestoreStateErrorItem = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_error = el.find("error")
    if child_error is not None:
        import capo_ec2.types.disable_fast_snapshot_restore_state_error

        out["error"] = (
            capo_ec2.types.disable_fast_snapshot_restore_state_error.deserialize_ec2_query(
                child_error
            )
        )
    return out
