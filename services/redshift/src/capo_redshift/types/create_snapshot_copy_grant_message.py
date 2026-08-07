"""Generated from Smithy shape ``com.amazonaws.redshift#CreateSnapshotCopyGrantMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string
    import capo_redshift.types.tag_list


class CreateSnapshotCopyGrantMessage(TypedDict, closed=True):
    snapshot_copy_grant_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the snapshot copy grant. This name must be unique in the region for the Amazon Web Services account.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 alphanumeric characters or hyphens.</p> </li> <li> <p>Alphabetic characters must be lowercase.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Must be unique for all clusters within an Amazon Web Services account.</p> </li> </ul>"""
    kms_key_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier of the encrypted symmetric key to which to grant Amazon Redshift permission. If no key is specified, the default key is used.</p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>A list of tag instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateSnapshotCopyGrantMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "snapshot_copy_grant_name" in value:
        pairs.append(
            (
                f"{key_prefix}SnapshotCopyGrantName",
                str(value["snapshot_copy_grant_name"]),
            )
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "tags" in value:
        import capo_redshift.types.tag_list

        capo_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateSnapshotCopyGrantMessage:
    out: CreateSnapshotCopyGrantMessage = {}  # type: ignore[typeddict-item]
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
