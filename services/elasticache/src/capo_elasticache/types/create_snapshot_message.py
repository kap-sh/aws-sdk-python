"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string
    import capo_elasticache.types.tag_list


class CreateSnapshotMessage(TypedDict, closed=True):
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The identifier of an existing replication group. The snapshot is created from this replication group.</p>"""
    cache_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The identifier of an existing cluster. The snapshot is created from this cluster.</p>"""
    snapshot_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>A name for the snapshot being created. This value is stored as a lowercase string.</p>"""
    kms_key_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the KMS key used to encrypt the snapshot.</p>"""
    tags: NotRequired["capo_elasticache.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replication_group_id" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "cache_cluster_id" in value:
        pairs.append((f"{prefix}.CacheClusterId", str(value["cache_cluster_id"])))
    if "snapshot_name" in value:
        pairs.append((f"{prefix}.SnapshotName", str(value["snapshot_name"])))
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "tags" in value:
        import capo_elasticache.types.tag_list

        capo_elasticache.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateSnapshotMessage:
    out: CreateSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_snapshot_name = el.find("SnapshotName")
    if child_snapshot_name is not None:
        out["snapshot_name"] = str(child_snapshot_name.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elasticache.types.tag_list

        out["tags"] = capo_elasticache.types.tag_list.deserialize_query(child_tags)
    return out
