"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastSnapshotRestoresRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id_string_list
    import aws_sdk_ec2.types.availability_zone_string_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.snapshot_id_string_list


class DisableFastSnapshotRestoresRequest(TypedDict):
    availability_zones: NotRequired[
        "aws_sdk_ec2.types.availability_zone_string_list.AvailabilityZoneStringList"
    ]
    """<p>One or more Availability Zones. For example, <code>us-east-2a</code>.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""
    availability_zone_ids: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id_string_list.AvailabilityZoneIdStringList"
    ]
    """<p>One or more Availability Zone IDs. For example, <code>use2-az1</code>.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""
    source_snapshot_ids: NotRequired[
        "aws_sdk_ec2.types.snapshot_id_string_list.SnapshotIdStringList"
    ]
    """<p>The IDs of one or more snapshots. For example, <code>snap-1234567890abcdef0</code>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableFastSnapshotRestoresRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zones" in value:
        import aws_sdk_ec2.types.availability_zone_string_list

        aws_sdk_ec2.types.availability_zone_string_list.serialize_ec2_query(
            value["availability_zones"], pairs, f"{prefix}.AvailabilityZones"
        )
    if "availability_zone_ids" in value:
        import aws_sdk_ec2.types.availability_zone_id_string_list

        aws_sdk_ec2.types.availability_zone_id_string_list.serialize_ec2_query(
            value["availability_zone_ids"], pairs, f"{prefix}.AvailabilityZoneIds"
        )
    if "source_snapshot_ids" in value:
        import aws_sdk_ec2.types.snapshot_id_string_list

        aws_sdk_ec2.types.snapshot_id_string_list.serialize_ec2_query(
            value["source_snapshot_ids"], pairs, f"{prefix}.SourceSnapshotIds"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DisableFastSnapshotRestoresRequest:
    out: DisableFastSnapshotRestoresRequest = {}  # type: ignore[typeddict-item]
    if el.find("AvailabilityZones") is not None:
        import aws_sdk_ec2.types.availability_zone_string_list

        out["availability_zones"] = (
            aws_sdk_ec2.types.availability_zone_string_list.deserialize_ec2_query(
                el, "AvailabilityZones"
            )
        )
    if el.find("AvailabilityZoneIds") is not None:
        import aws_sdk_ec2.types.availability_zone_id_string_list

        out["availability_zone_ids"] = (
            aws_sdk_ec2.types.availability_zone_id_string_list.deserialize_ec2_query(
                el, "AvailabilityZoneIds"
            )
        )
    if el.find("SourceSnapshotIds") is not None:
        import aws_sdk_ec2.types.snapshot_id_string_list

        out["source_snapshot_ids"] = (
            aws_sdk_ec2.types.snapshot_id_string_list.deserialize_ec2_query(
                el, "SourceSnapshotIds"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
