"""Generated from Smithy shape ``com.amazonaws.ec2#ResetSnapshotAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.snapshot_attribute_name
    import capo_ec2.types.snapshot_id


class ResetSnapshotAttributeRequest(TypedDict, closed=True):
    attribute: NotRequired[
        "capo_ec2.types.snapshot_attribute_name.SnapshotAttributeName"
    ]
    """<p>The attribute to reset. Currently, only the attribute for permission to create volumes can be reset.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResetSnapshotAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attribute" in value:
        import capo_ec2.types.snapshot_attribute_name

        capo_ec2.types.snapshot_attribute_name.serialize_ec2_query(
            value["attribute"], pairs, f"{prefix}.Attribute"
        )
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ResetSnapshotAttributeRequest:
    out: ResetSnapshotAttributeRequest = {}  # type: ignore[typeddict-item]
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        import capo_ec2.types.snapshot_attribute_name

        out["attribute"] = capo_ec2.types.snapshot_attribute_name.deserialize_ec2_query(
            child_attribute
        )
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
