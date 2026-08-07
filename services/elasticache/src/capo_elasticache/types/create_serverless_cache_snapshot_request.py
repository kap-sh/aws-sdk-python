"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateServerlessCacheSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string
    import capo_elasticache.types.tag_list


class CreateServerlessCacheSnapshotRequest(TypedDict, closed=True):
    serverless_cache_snapshot_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name for the snapshot being created. Must be unique for the customer account. Available for Valkey, Redis OSS and Serverless Memcached only. Must be between 1 and 255 characters. This value is stored as a lowercase string.</p>"""
    serverless_cache_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of an existing serverless cache. The snapshot is created from this cache. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    kms_key_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the KMS key used to encrypt the snapshot. Available for Valkey, Redis OSS and Serverless Memcached only. Default: NULL</p>"""
    tags: NotRequired["capo_elasticache.types.tag_list.TagList"]
    """<p>A list of tags to be added to the snapshot resource. A tag is a key-value pair. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateServerlessCacheSnapshotRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "serverless_cache_snapshot_name" in value:
        pairs.append(
            (
                f"{key_prefix}ServerlessCacheSnapshotName",
                str(value["serverless_cache_snapshot_name"]),
            )
        )
    if "serverless_cache_name" in value:
        pairs.append(
            (f"{key_prefix}ServerlessCacheName", str(value["serverless_cache_name"]))
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "tags" in value:
        import capo_elasticache.types.tag_list

        capo_elasticache.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateServerlessCacheSnapshotRequest:
    out: CreateServerlessCacheSnapshotRequest = {}  # type: ignore[typeddict-item]
    child_serverless_cache_snapshot_name = el.find("ServerlessCacheSnapshotName")
    if child_serverless_cache_snapshot_name is not None:
        out["serverless_cache_snapshot_name"] = str(
            child_serverless_cache_snapshot_name.text or ""
        )
    child_serverless_cache_name = el.find("ServerlessCacheName")
    if child_serverless_cache_name is not None:
        out["serverless_cache_name"] = str(child_serverless_cache_name.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elasticache.types.tag_list

        out["tags"] = capo_elasticache.types.tag_list.deserialize_query(child_tags)
    return out
