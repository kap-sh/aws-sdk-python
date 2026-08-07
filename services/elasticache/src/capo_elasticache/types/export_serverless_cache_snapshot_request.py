"""Generated from Smithy shape ``com.amazonaws.elasticache#ExportServerlessCacheSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class ExportServerlessCacheSnapshotRequest(TypedDict, closed=True):
    serverless_cache_snapshot_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The identifier of the serverless cache snapshot to be exported to S3. Available for Valkey and Redis OSS only.</p>"""
    s3_bucket_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>Name of the Amazon S3 bucket to export the snapshot to. The Amazon S3 bucket must also be in same region as the snapshot. Available for Valkey and Redis OSS only.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ExportServerlessCacheSnapshotRequest,
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
    if "s3_bucket_name" in value:
        pairs.append((f"{key_prefix}S3BucketName", str(value["s3_bucket_name"])))


def deserialize_query(el: Element) -> ExportServerlessCacheSnapshotRequest:
    out: ExportServerlessCacheSnapshotRequest = {}  # type: ignore[typeddict-item]
    child_serverless_cache_snapshot_name = el.find("ServerlessCacheSnapshotName")
    if child_serverless_cache_snapshot_name is not None:
        out["serverless_cache_snapshot_name"] = str(
            child_serverless_cache_snapshot_name.text or ""
        )
    child_s3_bucket_name = el.find("S3BucketName")
    if child_s3_bucket_name is not None:
        out["s3_bucket_name"] = str(child_s3_bucket_name.text or "")
    return out
