"""Generated from Smithy shape ``com.amazonaws.elasticache#ModifyServerlessCacheRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.cache_usage_limits
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.security_group_ids_list
    import capo_elasticache.types.string


class ModifyServerlessCacheRequest(TypedDict, closed=True):
    serverless_cache_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>User-provided identifier for the serverless cache to be modified.</p>"""
    description: NotRequired["capo_elasticache.types.string.String"]
    """<p>User provided description for the serverless cache. Default = NULL, i.e. the existing description is not removed/modified. The description has a maximum length of 255 characters.</p>"""
    cache_usage_limits: NotRequired[
        "capo_elasticache.types.cache_usage_limits.CacheUsageLimits"
    ]
    """<p>Modify the cache usage limit for the serverless cache.</p>"""
    remove_user_group: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>The identifier of the UserGroup to be removed from association with the Valkey and Redis OSS serverless cache. Available for Valkey and Redis OSS only. Default is NULL.</p>"""
    user_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The identifier of the UserGroup to be associated with the serverless cache. Available for Valkey and Redis OSS only. Default is NULL - the existing UserGroup is not removed.</p>"""
    security_group_ids: NotRequired[
        "capo_elasticache.types.security_group_ids_list.SecurityGroupIdsList"
    ]
    """<p>The new list of VPC security groups to be associated with the serverless cache. Populating this list means the current VPC security groups will be removed. This security group is used to authorize traffic access for the VPC end-point (private-link). Default = NULL - the existing list of VPC security groups is not removed.</p>"""
    snapshot_retention_limit: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which Elasticache retains automatic snapshots before deleting them. Available for Valkey, Redis OSS and Serverless Memcached only. Default = NULL, i.e. the existing snapshot-retention-limit will not be removed or modified. The maximum value allowed is 35 days.</p>"""
    daily_snapshot_time: NotRequired["capo_elasticache.types.string.String"]
    """<p>The daily time during which Elasticache begins taking a daily snapshot of the serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only. The default is NULL, i.e. the existing snapshot time configured for the cluster is not removed.</p>"""
    engine: NotRequired["capo_elasticache.types.string.String"]
    """<p>Modifies the engine listed in a serverless cache request. The options are valkey, memcached or redis.</p>"""
    major_engine_version: NotRequired["capo_elasticache.types.string.String"]
    """<p>Modifies the engine vesion listed in a serverless cache request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyServerlessCacheRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "serverless_cache_name" in value:
        pairs.append(
            (f"{prefix}.ServerlessCacheName", str(value["serverless_cache_name"]))
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "cache_usage_limits" in value:
        import capo_elasticache.types.cache_usage_limits

        capo_elasticache.types.cache_usage_limits.serialize_query(
            value["cache_usage_limits"], pairs, f"{prefix}.CacheUsageLimits"
        )
    if "remove_user_group" in value:
        pairs.append(
            (
                f"{prefix}.RemoveUserGroup",
                "true" if value["remove_user_group"] else "false",
            )
        )
    if "user_group_id" in value:
        pairs.append((f"{prefix}.UserGroupId", str(value["user_group_id"])))
    if "security_group_ids" in value:
        import capo_elasticache.types.security_group_ids_list

        capo_elasticache.types.security_group_ids_list.serialize_query(
            value["security_group_ids"], pairs, f"{prefix}.SecurityGroupIds"
        )
    if "snapshot_retention_limit" in value:
        pairs.append(
            (f"{prefix}.SnapshotRetentionLimit", str(value["snapshot_retention_limit"]))
        )
    if "daily_snapshot_time" in value:
        pairs.append((f"{prefix}.DailySnapshotTime", str(value["daily_snapshot_time"])))
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "major_engine_version" in value:
        pairs.append(
            (f"{prefix}.MajorEngineVersion", str(value["major_engine_version"]))
        )


def deserialize_query(el: Element) -> ModifyServerlessCacheRequest:
    out: ModifyServerlessCacheRequest = {}  # type: ignore[typeddict-item]
    child_serverless_cache_name = el.find("ServerlessCacheName")
    if child_serverless_cache_name is not None:
        out["serverless_cache_name"] = str(child_serverless_cache_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_cache_usage_limits = el.find("CacheUsageLimits")
    if child_cache_usage_limits is not None:
        import capo_elasticache.types.cache_usage_limits

        out["cache_usage_limits"] = (
            capo_elasticache.types.cache_usage_limits.deserialize_query(
                child_cache_usage_limits
            )
        )
    child_remove_user_group = el.find("RemoveUserGroup")
    if child_remove_user_group is not None:
        out["remove_user_group"] = (
            child_remove_user_group.text or ""
        ).lower() == "true"
    child_user_group_id = el.find("UserGroupId")
    if child_user_group_id is not None:
        out["user_group_id"] = str(child_user_group_id.text or "")
    child_security_group_ids = el.find("SecurityGroupIds")
    if child_security_group_ids is not None:
        import capo_elasticache.types.security_group_ids_list

        out["security_group_ids"] = (
            capo_elasticache.types.security_group_ids_list.deserialize_query(
                child_security_group_ids
            )
        )
    child_snapshot_retention_limit = el.find("SnapshotRetentionLimit")
    if child_snapshot_retention_limit is not None:
        out["snapshot_retention_limit"] = int(child_snapshot_retention_limit.text or "")
    child_daily_snapshot_time = el.find("DailySnapshotTime")
    if child_daily_snapshot_time is not None:
        out["daily_snapshot_time"] = str(child_daily_snapshot_time.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_major_engine_version = el.find("MajorEngineVersion")
    if child_major_engine_version is not None:
        out["major_engine_version"] = str(child_major_engine_version.text or "")
    return out
