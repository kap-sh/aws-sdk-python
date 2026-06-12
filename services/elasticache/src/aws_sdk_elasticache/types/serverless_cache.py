"""Generated from Smithy shape ``com.amazonaws.elasticache#ServerlessCache``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_usage_limits
    import aws_sdk_elasticache.types.endpoint
    import aws_sdk_elasticache.types.integer_optional
    import aws_sdk_elasticache.types.network_type
    import aws_sdk_elasticache.types.security_group_ids_list
    import aws_sdk_elasticache.types.storage_encryption_type
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.subnet_ids_list
    import aws_sdk_elasticache.types.t_stamp


class ServerlessCache(TypedDict):
    serverless_cache_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The unique identifier of the serverless cache.</p>"""
    description: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>A description of the serverless cache.</p>"""
    create_time: NotRequired["aws_sdk_elasticache.types.t_stamp.TStamp"]
    """<p>When the serverless cache was created. </p>"""
    status: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The current status of the serverless cache. The allowed values are CREATING, AVAILABLE, DELETING, CREATE-FAILED and MODIFYING.</p>"""
    engine: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The engine the serverless cache is compatible with.</p>"""
    major_engine_version: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The version number of the engine the serverless cache is compatible with.</p>"""
    full_engine_version: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name and version number of the engine the serverless cache is compatible with.</p>"""
    cache_usage_limits: NotRequired[
        "aws_sdk_elasticache.types.cache_usage_limits.CacheUsageLimits"
    ]
    """<p>The cache usage limit for the serverless cache.</p>"""
    kms_key_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The ID of the Amazon Web Services Key Management Service (KMS) key that is used to encrypt data at rest in the serverless cache.</p>"""
    storage_encryption_type: NotRequired[
        "aws_sdk_elasticache.types.storage_encryption_type.StorageEncryptionType"
    ]
    """<p>Indicates the type of encryption for data stored at rest in the serverless cache. Serverless caches are always encrypted at rest. The value is <code>sse-elasticache</code> if an ElastiCache service-managed key is used, or <code>sse-kms</code> if a customer-managed KMS key is used.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_elasticache.types.security_group_ids_list.SecurityGroupIdsList"
    ]
    """<p>The IDs of the EC2 security groups associated with the serverless cache.</p>"""
    endpoint: NotRequired["aws_sdk_elasticache.types.endpoint.Endpoint"]
    reader_endpoint: NotRequired["aws_sdk_elasticache.types.endpoint.Endpoint"]
    arn: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the serverless cache.</p>"""
    user_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The identifier of the user group associated with the serverless cache. Available for Valkey and Redis OSS only. Default is NULL.</p>"""
    subnet_ids: NotRequired["aws_sdk_elasticache.types.subnet_ids_list.SubnetIdsList"]
    """<p>If no subnet IDs are given and your VPC is in us-west-1, then ElastiCache will select 2 default subnets across AZs in your VPC. For all other Regions, if no subnet IDs are given then ElastiCache will select 3 default subnets across AZs in your default VPC.</p>"""
    snapshot_retention_limit: NotRequired[
        "aws_sdk_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which ElastiCache retains automatic snapshots before deleting them. Available for Valkey, Redis OSS and Serverless Memcached only. The maximum value allowed is 35 days.</p>"""
    daily_snapshot_time: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The daily time that a cache snapshot will be created. Default is NULL, i.e. snapshots will not be created at a specific time on a daily basis. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    network_type: NotRequired["aws_sdk_elasticache.types.network_type.NetworkType"]
    """<p>The type of IP address protocol used by the serverless cache. Must be either <code>ipv4</code> | <code>ipv6</code> | <code>dual_stack</code>. <code>ipv6</code> is only supported with IPv6-only subnets. If not specified, defaults to <code>ipv4</code>, unless all provided subnets are IPv6-only, in which case it defaults to <code>ipv6</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessCache, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "serverless_cache_name" in value:
        pairs.append(
            (f"{prefix}.ServerlessCacheName", str(value["serverless_cache_name"]))
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "create_time" in value:
        import aws_sdk_elasticache.types.t_stamp

        aws_sdk_elasticache.types.t_stamp.serialize_query(
            value["create_time"], pairs, f"{prefix}.CreateTime"
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "major_engine_version" in value:
        pairs.append(
            (f"{prefix}.MajorEngineVersion", str(value["major_engine_version"]))
        )
    if "full_engine_version" in value:
        pairs.append((f"{prefix}.FullEngineVersion", str(value["full_engine_version"])))
    if "cache_usage_limits" in value:
        import aws_sdk_elasticache.types.cache_usage_limits

        aws_sdk_elasticache.types.cache_usage_limits.serialize_query(
            value["cache_usage_limits"], pairs, f"{prefix}.CacheUsageLimits"
        )
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "storage_encryption_type" in value:
        import aws_sdk_elasticache.types.storage_encryption_type

        aws_sdk_elasticache.types.storage_encryption_type.serialize_query(
            value["storage_encryption_type"], pairs, f"{prefix}.StorageEncryptionType"
        )
    if "security_group_ids" in value:
        import aws_sdk_elasticache.types.security_group_ids_list

        aws_sdk_elasticache.types.security_group_ids_list.serialize_query(
            value["security_group_ids"], pairs, f"{prefix}.SecurityGroupIds"
        )
    if "endpoint" in value:
        import aws_sdk_elasticache.types.endpoint

        aws_sdk_elasticache.types.endpoint.serialize_query(
            value["endpoint"], pairs, f"{prefix}.Endpoint"
        )
    if "reader_endpoint" in value:
        import aws_sdk_elasticache.types.endpoint

        aws_sdk_elasticache.types.endpoint.serialize_query(
            value["reader_endpoint"], pairs, f"{prefix}.ReaderEndpoint"
        )
    if "arn" in value:
        pairs.append((f"{prefix}.ARN", str(value["arn"])))
    if "user_group_id" in value:
        pairs.append((f"{prefix}.UserGroupId", str(value["user_group_id"])))
    if "subnet_ids" in value:
        import aws_sdk_elasticache.types.subnet_ids_list

        aws_sdk_elasticache.types.subnet_ids_list.serialize_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIds"
        )
    if "snapshot_retention_limit" in value:
        pairs.append(
            (f"{prefix}.SnapshotRetentionLimit", str(value["snapshot_retention_limit"]))
        )
    if "daily_snapshot_time" in value:
        pairs.append((f"{prefix}.DailySnapshotTime", str(value["daily_snapshot_time"])))
    if "network_type" in value:
        import aws_sdk_elasticache.types.network_type

        aws_sdk_elasticache.types.network_type.serialize_query(
            value["network_type"], pairs, f"{prefix}.NetworkType"
        )


def deserialize_query(el: Element) -> ServerlessCache:
    out: ServerlessCache = {}  # type: ignore[typeddict-item]
    child_serverless_cache_name = el.find("ServerlessCacheName")
    if child_serverless_cache_name is not None:
        out["serverless_cache_name"] = str(child_serverless_cache_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_create_time = el.find("CreateTime")
    if child_create_time is not None:
        import aws_sdk_elasticache.types.t_stamp

        out["create_time"] = aws_sdk_elasticache.types.t_stamp.deserialize_query(
            child_create_time
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_major_engine_version = el.find("MajorEngineVersion")
    if child_major_engine_version is not None:
        out["major_engine_version"] = str(child_major_engine_version.text or "")
    child_full_engine_version = el.find("FullEngineVersion")
    if child_full_engine_version is not None:
        out["full_engine_version"] = str(child_full_engine_version.text or "")
    child_cache_usage_limits = el.find("CacheUsageLimits")
    if child_cache_usage_limits is not None:
        import aws_sdk_elasticache.types.cache_usage_limits

        out["cache_usage_limits"] = (
            aws_sdk_elasticache.types.cache_usage_limits.deserialize_query(
                child_cache_usage_limits
            )
        )
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_storage_encryption_type = el.find("StorageEncryptionType")
    if child_storage_encryption_type is not None:
        import aws_sdk_elasticache.types.storage_encryption_type

        out["storage_encryption_type"] = (
            aws_sdk_elasticache.types.storage_encryption_type.deserialize_query(
                child_storage_encryption_type
            )
        )
    child_security_group_ids = el.find("SecurityGroupIds")
    if child_security_group_ids is not None:
        import aws_sdk_elasticache.types.security_group_ids_list

        out["security_group_ids"] = (
            aws_sdk_elasticache.types.security_group_ids_list.deserialize_query(
                child_security_group_ids
            )
        )
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        import aws_sdk_elasticache.types.endpoint

        out["endpoint"] = aws_sdk_elasticache.types.endpoint.deserialize_query(
            child_endpoint
        )
    child_reader_endpoint = el.find("ReaderEndpoint")
    if child_reader_endpoint is not None:
        import aws_sdk_elasticache.types.endpoint

        out["reader_endpoint"] = aws_sdk_elasticache.types.endpoint.deserialize_query(
            child_reader_endpoint
        )
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_user_group_id = el.find("UserGroupId")
    if child_user_group_id is not None:
        out["user_group_id"] = str(child_user_group_id.text or "")
    child_subnet_ids = el.find("SubnetIds")
    if child_subnet_ids is not None:
        import aws_sdk_elasticache.types.subnet_ids_list

        out["subnet_ids"] = aws_sdk_elasticache.types.subnet_ids_list.deserialize_query(
            child_subnet_ids
        )
    child_snapshot_retention_limit = el.find("SnapshotRetentionLimit")
    if child_snapshot_retention_limit is not None:
        out["snapshot_retention_limit"] = int(child_snapshot_retention_limit.text or "")
    child_daily_snapshot_time = el.find("DailySnapshotTime")
    if child_daily_snapshot_time is not None:
        out["daily_snapshot_time"] = str(child_daily_snapshot_time.text or "")
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        import aws_sdk_elasticache.types.network_type

        out["network_type"] = aws_sdk_elasticache.types.network_type.deserialize_query(
            child_network_type
        )
    return out
