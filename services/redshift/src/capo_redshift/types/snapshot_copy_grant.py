"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotCopyGrant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string
    import capo_redshift.types.tag_list


class SnapshotCopyGrant(TypedDict, closed=True):
    snapshot_copy_grant_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the snapshot copy grant.</p>"""
    kms_key_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier of the encrypted symmetric key in Amazon Web Services KMS to which Amazon Redshift is granted permission.</p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>A list of tag instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotCopyGrant, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_copy_grant_name" in value:
        pairs.append(
            (f"{prefix}.SnapshotCopyGrantName", str(value["snapshot_copy_grant_name"]))
        )
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "tags" in value:
        import capo_redshift.types.tag_list

        capo_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> SnapshotCopyGrant:
    out: SnapshotCopyGrant = {}  # type: ignore[typeddict-item]
    child_snapshot_copy_grant_name = el.find("SnapshotCopyGrantName")
    if child_snapshot_copy_grant_name is not None:
        out["snapshot_copy_grant_name"] = str(child_snapshot_copy_grant_name.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_redshift.types.tag_list

        out["tags"] = capo_redshift.types.tag_list.deserialize_query(child_tags)
    return out
