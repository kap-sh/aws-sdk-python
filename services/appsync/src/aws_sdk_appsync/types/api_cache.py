"""Generated from Smithy shape ``com.amazonaws.appsync#ApiCache``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.api_cache_status
    import aws_sdk_appsync.types.api_cache_type
    import aws_sdk_appsync.types.api_caching_behavior
    import aws_sdk_appsync.types.boolean
    import aws_sdk_appsync.types.cache_health_metrics_config
    import aws_sdk_appsync.types.long


class ApiCache(TypedDict):
    ttl: "aws_sdk_appsync.types.long.Long"
    """<p>TTL in seconds for cache entries.</p> <p>Valid values are 1–3,600 seconds.</p>"""
    api_caching_behavior: NotRequired[
        "aws_sdk_appsync.types.api_caching_behavior.ApiCachingBehavior"
    ]
    """<p>Caching behavior.</p> <ul> <li> <p> <b>FULL_REQUEST_CACHING</b>: All requests from the same user are cached. Individual resolvers are automatically cached. All API calls will try to return responses from the cache.</p> </li> <li> <p> <b>PER_RESOLVER_CACHING</b>: Individual resolvers that you specify are cached.</p> </li> <li> <p> <b>OPERATION_LEVEL_CACHING</b>: Full requests are cached together and returned without executing resolvers.</p> </li> </ul>"""
    transit_encryption_enabled: "aws_sdk_appsync.types.boolean.Boolean"
    """<p>Transit encryption flag when connecting to cache. You cannot update this setting after creation.</p>"""
    at_rest_encryption_enabled: "aws_sdk_appsync.types.boolean.Boolean"
    """<p>At-rest encryption flag for cache. You cannot update this setting after creation.</p>"""
    type: NotRequired["aws_sdk_appsync.types.api_cache_type.ApiCacheType"]
    """<p>The cache instance type. Valid values are </p> <ul> <li> <p> <code>SMALL</code> </p> </li> <li> <p> <code>MEDIUM</code> </p> </li> <li> <p> <code>LARGE</code> </p> </li> <li> <p> <code>XLARGE</code> </p> </li> <li> <p> <code>LARGE_2X</code> </p> </li> <li> <p> <code>LARGE_4X</code> </p> </li> <li> <p> <code>LARGE_8X</code> (not available in all regions)</p> </li> <li> <p> <code>LARGE_12X</code> </p> </li> </ul> <p>Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used.</p> <p>The following legacy instance types are available, but their use is discouraged:</p> <ul> <li> <p> <b>T2_SMALL</b>: A t2.small instance type.</p> </li> <li> <p> <b>T2_MEDIUM</b>: A t2.medium instance type.</p> </li> <li> <p> <b>R4_LARGE</b>: A r4.large instance type.</p> </li> <li> <p> <b>R4_XLARGE</b>: A r4.xlarge instance type.</p> </li> <li> <p> <b>R4_2XLARGE</b>: A r4.2xlarge instance type.</p> </li> <li> <p> <b>R4_4XLARGE</b>: A r4.4xlarge instance type.</p> </li> <li> <p> <b>R4_8XLARGE</b>: A r4.8xlarge instance type.</p> </li> </ul>"""
    status: NotRequired["aws_sdk_appsync.types.api_cache_status.ApiCacheStatus"]
    """<p>The cache instance status.</p> <ul> <li> <p> <b>AVAILABLE</b>: The instance is available for use.</p> </li> <li> <p> <b>CREATING</b>: The instance is currently creating.</p> </li> <li> <p> <b>DELETING</b>: The instance is currently deleting.</p> </li> <li> <p> <b>MODIFYING</b>: The instance is currently modifying.</p> </li> <li> <p> <b>FAILED</b>: The instance has failed creation.</p> </li> </ul>"""
    health_metrics_config: NotRequired[
        "aws_sdk_appsync.types.cache_health_metrics_config.CacheHealthMetricsConfig"
    ]
    """<p>Controls how cache health metrics will be emitted to CloudWatch. Cache health metrics include:</p> <ul> <li> <p>NetworkBandwidthOutAllowanceExceeded: The network packets dropped because the throughput exceeded the aggregated bandwidth limit. This is useful for diagnosing bottlenecks in a cache configuration.</p> </li> <li> <p>EngineCPUUtilization: The CPU utilization (percentage) allocated to the Redis process. This is useful for diagnosing bottlenecks in a cache configuration.</p> </li> </ul> <p>Metrics will be recorded by API ID. You can set the value to <code>ENABLED</code> or <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiCache) -> dict:
    out: dict = {}
    out["ttl"] = value.get("ttl", 0)
    if "api_caching_behavior" in value:
        import aws_sdk_appsync.types.api_caching_behavior

        out["apiCachingBehavior"] = (
            aws_sdk_appsync.types.api_caching_behavior.serialize_json(
                value["api_caching_behavior"]
            )
        )
    out["transitEncryptionEnabled"] = value.get("transit_encryption_enabled", False)
    out["atRestEncryptionEnabled"] = value.get("at_rest_encryption_enabled", False)
    if "type" in value:
        import aws_sdk_appsync.types.api_cache_type

        out["type"] = aws_sdk_appsync.types.api_cache_type.serialize_json(value["type"])
    if "status" in value:
        import aws_sdk_appsync.types.api_cache_status

        out["status"] = aws_sdk_appsync.types.api_cache_status.serialize_json(
            value["status"]
        )
    if "health_metrics_config" in value:
        import aws_sdk_appsync.types.cache_health_metrics_config

        out["healthMetricsConfig"] = (
            aws_sdk_appsync.types.cache_health_metrics_config.serialize_json(
                value["health_metrics_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApiCache:
    out: ApiCache = {}  # type: ignore[typeddict-item]
    if "ttl" in data:
        out["ttl"] = data["ttl"]
    else:
        out["ttl"] = 0
    if "apiCachingBehavior" in data:
        import aws_sdk_appsync.types.api_caching_behavior

        out["api_caching_behavior"] = (
            aws_sdk_appsync.types.api_caching_behavior.deserialize_json(
                data["apiCachingBehavior"]
            )
        )
    if "transitEncryptionEnabled" in data:
        out["transit_encryption_enabled"] = data["transitEncryptionEnabled"]
    else:
        out["transit_encryption_enabled"] = False
    if "atRestEncryptionEnabled" in data:
        out["at_rest_encryption_enabled"] = data["atRestEncryptionEnabled"]
    else:
        out["at_rest_encryption_enabled"] = False
    if "type" in data:
        import aws_sdk_appsync.types.api_cache_type

        out["type"] = aws_sdk_appsync.types.api_cache_type.deserialize_json(
            data["type"]
        )
    if "status" in data:
        import aws_sdk_appsync.types.api_cache_status

        out["status"] = aws_sdk_appsync.types.api_cache_status.deserialize_json(
            data["status"]
        )
    if "healthMetricsConfig" in data:
        import aws_sdk_appsync.types.cache_health_metrics_config

        out["health_metrics_config"] = (
            aws_sdk_appsync.types.cache_health_metrics_config.deserialize_json(
                data["healthMetricsConfig"]
            )
        )
    return out
