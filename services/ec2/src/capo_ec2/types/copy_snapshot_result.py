"""Generated from Smithy shape ``com.amazonaws.ec2#CopySnapshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class CopySnapshotResult(TypedDict, closed=True):
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags applied to the new snapshot.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the new snapshot.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CopySnapshotResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))


def deserialize_ec2_query(el: Element) -> CopySnapshotResult:
    out: CopySnapshotResult = {}  # type: ignore[typeddict-item]
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    return out
