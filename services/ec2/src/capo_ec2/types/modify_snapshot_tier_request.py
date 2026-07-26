"""Generated from Smithy shape ``com.amazonaws.ec2#ModifySnapshotTierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.snapshot_id
    import capo_ec2.types.target_storage_tier


class ModifySnapshotTierRequest(TypedDict, closed=True):
    snapshot_id: NotRequired["capo_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    storage_tier: NotRequired["capo_ec2.types.target_storage_tier.TargetStorageTier"]
    """<p>The name of the storage tier. You must specify <code>archive</code>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifySnapshotTierRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "storage_tier" in value:
        import capo_ec2.types.target_storage_tier

        capo_ec2.types.target_storage_tier.serialize_ec2_query(
            value["storage_tier"], pairs, f"{prefix}.StorageTier"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifySnapshotTierRequest:
    out: ModifySnapshotTierRequest = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_storage_tier = el.find("StorageTier")
    if child_storage_tier is not None:
        import capo_ec2.types.target_storage_tier

        out["storage_tier"] = capo_ec2.types.target_storage_tier.deserialize_ec2_query(
            child_storage_tier
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
