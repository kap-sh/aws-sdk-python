"""Generated from Smithy shape ``com.amazonaws.elasticache#ServerlessCacheSnapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.serverless_cache_configuration
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.t_stamp


class ServerlessCacheSnapshot(TypedDict, closed=True):
    serverless_cache_snapshot_name: NotRequired[
        "aws_sdk_elasticache.types.string.String"
    ]
    """<p>The identifier of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    arn: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    kms_key_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The ID of the Amazon Web Services Key Management Service (KMS) key of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    snapshot_type: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The type of snapshot of serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    status: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The current status of the serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    create_time: NotRequired["aws_sdk_elasticache.types.t_stamp.TStamp"]
    """<p>The date and time that the source serverless cache's metadata and cache data set was obtained for the snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    expiry_time: NotRequired["aws_sdk_elasticache.types.t_stamp.TStamp"]
    """<p>The time that the serverless cache snapshot will expire. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    bytes_used_for_cache: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The total size of a serverless cache snapshot, in bytes. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    serverless_cache_configuration: NotRequired[
        "aws_sdk_elasticache.types.serverless_cache_configuration.ServerlessCacheConfiguration"
    ]
    """<p>The configuration of the serverless cache, at the time the snapshot was taken. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessCacheSnapshot, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "serverless_cache_snapshot_name" in value:
        pairs.append(
            (
                f"{prefix}.ServerlessCacheSnapshotName",
                str(value["serverless_cache_snapshot_name"]),
            )
        )
    if "arn" in value:
        pairs.append((f"{prefix}.ARN", str(value["arn"])))
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "snapshot_type" in value:
        pairs.append((f"{prefix}.SnapshotType", str(value["snapshot_type"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "create_time" in value:
        import aws_sdk_elasticache.types.t_stamp

        aws_sdk_elasticache.types.t_stamp.serialize_query(
            value["create_time"], pairs, f"{prefix}.CreateTime"
        )
    if "expiry_time" in value:
        import aws_sdk_elasticache.types.t_stamp

        aws_sdk_elasticache.types.t_stamp.serialize_query(
            value["expiry_time"], pairs, f"{prefix}.ExpiryTime"
        )
    if "bytes_used_for_cache" in value:
        pairs.append(
            (f"{prefix}.BytesUsedForCache", str(value["bytes_used_for_cache"]))
        )
    if "serverless_cache_configuration" in value:
        import aws_sdk_elasticache.types.serverless_cache_configuration

        aws_sdk_elasticache.types.serverless_cache_configuration.serialize_query(
            value["serverless_cache_configuration"],
            pairs,
            f"{prefix}.ServerlessCacheConfiguration",
        )


def deserialize_query(el: Element) -> ServerlessCacheSnapshot:
    out: ServerlessCacheSnapshot = {}  # type: ignore[typeddict-item]
    child_serverless_cache_snapshot_name = el.find("ServerlessCacheSnapshotName")
    if child_serverless_cache_snapshot_name is not None:
        out["serverless_cache_snapshot_name"] = str(
            child_serverless_cache_snapshot_name.text or ""
        )
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_snapshot_type = el.find("SnapshotType")
    if child_snapshot_type is not None:
        out["snapshot_type"] = str(child_snapshot_type.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_create_time = el.find("CreateTime")
    if child_create_time is not None:
        import aws_sdk_elasticache.types.t_stamp

        out["create_time"] = aws_sdk_elasticache.types.t_stamp.deserialize_query(
            child_create_time
        )
    child_expiry_time = el.find("ExpiryTime")
    if child_expiry_time is not None:
        import aws_sdk_elasticache.types.t_stamp

        out["expiry_time"] = aws_sdk_elasticache.types.t_stamp.deserialize_query(
            child_expiry_time
        )
    child_bytes_used_for_cache = el.find("BytesUsedForCache")
    if child_bytes_used_for_cache is not None:
        out["bytes_used_for_cache"] = str(child_bytes_used_for_cache.text or "")
    child_serverless_cache_configuration = el.find("ServerlessCacheConfiguration")
    if child_serverless_cache_configuration is not None:
        import aws_sdk_elasticache.types.serverless_cache_configuration

        out["serverless_cache_configuration"] = (
            aws_sdk_elasticache.types.serverless_cache_configuration.deserialize_query(
                child_serverless_cache_configuration
            )
        )
    return out
