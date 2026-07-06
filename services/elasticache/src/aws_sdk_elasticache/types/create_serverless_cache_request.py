"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateServerlessCacheRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_usage_limits
    import aws_sdk_elasticache.types.integer_optional
    import aws_sdk_elasticache.types.network_type
    import aws_sdk_elasticache.types.security_group_ids_list
    import aws_sdk_elasticache.types.snapshot_arns_list
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.subnet_ids_list
    import aws_sdk_elasticache.types.tag_list


class CreateServerlessCacheRequest(TypedDict, closed=True):
    serverless_cache_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>User-provided identifier for the serverless cache. This parameter is stored as a lowercase string.</p>"""
    description: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>User-provided description for the serverless cache. The default is NULL, i.e. if no description is provided then an empty string will be returned. The maximum length is 255 characters. </p>"""
    engine: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the cache engine to be used for creating the serverless cache.</p>"""
    major_engine_version: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The version of the cache engine that will be used to create the serverless cache.</p>"""
    cache_usage_limits: NotRequired[
        "aws_sdk_elasticache.types.cache_usage_limits.CacheUsageLimits"
    ]
    """<p>Sets the cache usage limits for storage and ElastiCache Processing Units for the cache.</p>"""
    kms_key_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>ARN of the customer managed key for encrypting the data at rest. If no KMS key is provided, a default service key is used.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_elasticache.types.security_group_ids_list.SecurityGroupIdsList"
    ]
    """<p>A list of the one or more VPC security groups to be associated with the serverless cache. The security group will authorize traffic access for the VPC end-point (private-link). If no other information is given this will be the VPC’s Default Security Group that is associated with the cluster VPC end-point.</p>"""
    snapshot_arns_to_restore: NotRequired[
        "aws_sdk_elasticache.types.snapshot_arns_list.SnapshotArnsList"
    ]
    """<p>The ARN(s) of the snapshot that the new serverless cache will be created from. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    tags: NotRequired["aws_sdk_elasticache.types.tag_list.TagList"]
    """<p>The list of tags (key, value) pairs to be added to the serverless cache resource. Default is NULL.</p>"""
    user_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The identifier of the UserGroup to be associated with the serverless cache. Available for Valkey and Redis OSS only. Default is NULL.</p>"""
    subnet_ids: NotRequired["aws_sdk_elasticache.types.subnet_ids_list.SubnetIdsList"]
    """<p>A list of the identifiers of the subnets where the VPC endpoint for the serverless cache will be deployed. All the subnetIds must belong to the same VPC.</p>"""
    snapshot_retention_limit: NotRequired[
        "aws_sdk_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which ElastiCache retains automatic snapshots before deleting them. Available for Valkey, Redis OSS and Serverless Memcached only. The maximum value allowed is 35 days.</p>"""
    daily_snapshot_time: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The daily time that snapshots will be created from the new serverless cache. By default this number is populated with 0, i.e. no snapshots will be created on an automatic daily basis. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    network_type: NotRequired["aws_sdk_elasticache.types.network_type.NetworkType"]
    """<p>The IP protocol version used by the serverless cache. Must be either <code>ipv4</code> | <code>ipv6</code> | <code>dual_stack</code>. <code>ipv6</code> is only supported with IPv6-only subnets. If not specified, defaults to <code>ipv4</code>, unless all provided subnets are IPv6-only, in which case it defaults to <code>ipv6</code>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateServerlessCacheRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "serverless_cache_name" in value:
        pairs.append(
            (f"{prefix}.ServerlessCacheName", str(value["serverless_cache_name"]))
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "major_engine_version" in value:
        pairs.append(
            (f"{prefix}.MajorEngineVersion", str(value["major_engine_version"]))
        )
    if "cache_usage_limits" in value:
        import aws_sdk_elasticache.types.cache_usage_limits

        aws_sdk_elasticache.types.cache_usage_limits.serialize_query(
            value["cache_usage_limits"], pairs, f"{prefix}.CacheUsageLimits"
        )
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "security_group_ids" in value:
        import aws_sdk_elasticache.types.security_group_ids_list

        aws_sdk_elasticache.types.security_group_ids_list.serialize_query(
            value["security_group_ids"], pairs, f"{prefix}.SecurityGroupIds"
        )
    if "snapshot_arns_to_restore" in value:
        import aws_sdk_elasticache.types.snapshot_arns_list

        aws_sdk_elasticache.types.snapshot_arns_list.serialize_query(
            value["snapshot_arns_to_restore"], pairs, f"{prefix}.SnapshotArnsToRestore"
        )
    if "tags" in value:
        import aws_sdk_elasticache.types.tag_list

        aws_sdk_elasticache.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )
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


def deserialize_query(el: Element) -> CreateServerlessCacheRequest:
    out: CreateServerlessCacheRequest = {}  # type: ignore[typeddict-item]
    child_serverless_cache_name = el.find("ServerlessCacheName")
    if child_serverless_cache_name is not None:
        out["serverless_cache_name"] = str(child_serverless_cache_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_major_engine_version = el.find("MajorEngineVersion")
    if child_major_engine_version is not None:
        out["major_engine_version"] = str(child_major_engine_version.text or "")
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
    child_security_group_ids = el.find("SecurityGroupIds")
    if child_security_group_ids is not None:
        import aws_sdk_elasticache.types.security_group_ids_list

        out["security_group_ids"] = (
            aws_sdk_elasticache.types.security_group_ids_list.deserialize_query(
                child_security_group_ids
            )
        )
    child_snapshot_arns_to_restore = el.find("SnapshotArnsToRestore")
    if child_snapshot_arns_to_restore is not None:
        import aws_sdk_elasticache.types.snapshot_arns_list

        out["snapshot_arns_to_restore"] = (
            aws_sdk_elasticache.types.snapshot_arns_list.deserialize_query(
                child_snapshot_arns_to_restore
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_elasticache.types.tag_list

        out["tags"] = aws_sdk_elasticache.types.tag_list.deserialize_query(child_tags)
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
