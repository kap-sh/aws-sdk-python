"""Generated from Smithy shape ``com.amazonaws.elasticache#CopyServerlessCacheSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string
    import capo_elasticache.types.tag_list


class CopyServerlessCacheSnapshotRequest(TypedDict, closed=True):
    source_serverless_cache_snapshot_name: NotRequired[
        "capo_elasticache.types.string.String"
    ]
    """<p>The identifier of the existing serverless cache’s snapshot to be copied. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    target_serverless_cache_snapshot_name: NotRequired[
        "capo_elasticache.types.string.String"
    ]
    """<p>The identifier for the snapshot to be created. Available for Valkey, Redis OSS and Serverless Memcached only. This value is stored as a lowercase string.</p>"""
    kms_key_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The identifier of the KMS key used to encrypt the target snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    tags: NotRequired["capo_elasticache.types.tag_list.TagList"]
    """<p>A list of tags to be added to the target snapshot resource. A tag is a key-value pair. Available for Valkey, Redis OSS and Serverless Memcached only. Default: NULL</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CopyServerlessCacheSnapshotRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_serverless_cache_snapshot_name" in value:
        pairs.append(
            (
                f"{prefix}.SourceServerlessCacheSnapshotName",
                str(value["source_serverless_cache_snapshot_name"]),
            )
        )
    if "target_serverless_cache_snapshot_name" in value:
        pairs.append(
            (
                f"{prefix}.TargetServerlessCacheSnapshotName",
                str(value["target_serverless_cache_snapshot_name"]),
            )
        )
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "tags" in value:
        import capo_elasticache.types.tag_list

        capo_elasticache.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CopyServerlessCacheSnapshotRequest:
    out: CopyServerlessCacheSnapshotRequest = {}  # type: ignore[typeddict-item]
    child_source_serverless_cache_snapshot_name = el.find(
        "SourceServerlessCacheSnapshotName"
    )
    if child_source_serverless_cache_snapshot_name is not None:
        out["source_serverless_cache_snapshot_name"] = str(
            child_source_serverless_cache_snapshot_name.text or ""
        )
    child_target_serverless_cache_snapshot_name = el.find(
        "TargetServerlessCacheSnapshotName"
    )
    if child_target_serverless_cache_snapshot_name is not None:
        out["target_serverless_cache_snapshot_name"] = str(
            child_target_serverless_cache_snapshot_name.text or ""
        )
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elasticache.types.tag_list

        out["tags"] = capo_elasticache.types.tag_list.deserialize_query(child_tags)
    return out
