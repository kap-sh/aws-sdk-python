"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastSnapshotRestoresRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_id_string_list
    import capo_ec2.types.availability_zone_string_list
    import capo_ec2.types.boolean
    import capo_ec2.types.snapshot_id_string_list


class EnableFastSnapshotRestoresRequest(TypedDict, closed=True):
    availability_zones: NotRequired[
        "capo_ec2.types.availability_zone_string_list.AvailabilityZoneStringList"
    ]
    """<p>One or more Availability Zones. For example, <code>us-east-2a</code>.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""
    availability_zone_ids: NotRequired[
        "capo_ec2.types.availability_zone_id_string_list.AvailabilityZoneIdStringList"
    ]
    """<p>One or more Availability Zone IDs. For example, <code>use2-az1</code>.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""
    source_snapshot_ids: NotRequired[
        "capo_ec2.types.snapshot_id_string_list.SnapshotIdStringList"
    ]
    """<p>The IDs of one or more snapshots. For example, <code>snap-1234567890abcdef0</code>. You can specify a snapshot that was shared with you from another Amazon Web Services account.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableFastSnapshotRestoresRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zones" in value:
        import capo_ec2.types.availability_zone_string_list

        capo_ec2.types.availability_zone_string_list.serialize_ec2_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZone"
        )
    if "availability_zone_ids" in value:
        import capo_ec2.types.availability_zone_id_string_list

        capo_ec2.types.availability_zone_id_string_list.serialize_ec2_query(
            value["availability_zone_ids"], pairs, f"{key_prefix}AvailabilityZoneId"
        )
    if "source_snapshot_ids" in value:
        import capo_ec2.types.snapshot_id_string_list

        capo_ec2.types.snapshot_id_string_list.serialize_ec2_query(
            value["source_snapshot_ids"], pairs, f"{key_prefix}SourceSnapshotId"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> EnableFastSnapshotRestoresRequest:
    out: EnableFastSnapshotRestoresRequest = {}  # type: ignore[typeddict-item]
    if el.find("AvailabilityZone") is not None:
        import capo_ec2.types.availability_zone_string_list

        out["availability_zones"] = (
            capo_ec2.types.availability_zone_string_list.deserialize_ec2_query(
                el, "AvailabilityZone"
            )
        )
    if el.find("AvailabilityZoneId") is not None:
        import capo_ec2.types.availability_zone_id_string_list

        out["availability_zone_ids"] = (
            capo_ec2.types.availability_zone_id_string_list.deserialize_ec2_query(
                el, "AvailabilityZoneId"
            )
        )
    if el.find("SourceSnapshotId") is not None:
        import capo_ec2.types.snapshot_id_string_list

        out["source_snapshot_ids"] = (
            capo_ec2.types.snapshot_id_string_list.deserialize_ec2_query(
                el, "SourceSnapshotId"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
