"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsApiGatewayMethodSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.double
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsApiGatewayMethodSettings(TypedDict, closed=True):
    metrics_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether CloudWatch metrics are enabled for the method. </p>"""
    logging_level: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The logging level for this method. The logging level affects the log entries that are pushed to CloudWatch Logs.</p> <p>If the logging level is <code>ERROR</code>, then the logs only include error-level entries.</p> <p>If the logging level is <code>INFO</code>, then the logs include both <code>ERROR</code> events and extra informational events.</p> <p>Valid values: <code>OFF</code> | <code>ERROR</code> | <code>INFO</code> </p>"""
    data_trace_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether data trace logging is enabled for the method. Data trace logging affects the log entries that are pushed to CloudWatch Logs.</p>"""
    throttling_burst_limit: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The throttling burst limit for the method.</p>"""
    throttling_rate_limit: NotRequired["capo_securityhub.types.double.Double"]
    """<p>The throttling rate limit for the method.</p>"""
    caching_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether responses are cached and returned for requests. For responses to be cached, a cache cluster must be enabled on the stage.</p>"""
    cache_ttl_in_seconds: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL, the longer the response is cached.</p>"""
    cache_data_encrypted: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the cached responses are encrypted. </p>"""
    require_authorization_for_cache_control: NotRequired[
        "capo_securityhub.types.boolean.Boolean"
    ]
    """<p>Indicates whether authorization is required for a cache invalidation request.</p>"""
    unauthorized_cache_control_header_strategy: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates how to handle unauthorized requests for cache invalidation.</p> <p>Valid values: <code>FAIL_WITH_403</code> | <code>SUCCEED_WITH_RESPONSE_HEADER</code> | <code>SUCCEED_WITHOUT_RESPONSE_HEADER</code> </p>"""
    http_method: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The HTTP method. You can use an asterisk (*) as a wildcard to apply method settings to multiple methods.</p>"""
    resource_path: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The resource path for this method. Forward slashes (/) are encoded as ~1 . The initial slash must include a forward slash.</p> <p>For example, the path value <code>/resource/subresource</code> must be encoded as <code>/~1resource~1subresource</code>.</p> <p>To specify the root path, use only a slash (/). You can use an asterisk (*) as a wildcard to apply method settings to multiple methods.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiGatewayMethodSettings) -> dict:
    out: dict = {}
    if "metrics_enabled" in value:
        out["MetricsEnabled"] = value["metrics_enabled"]
    if "logging_level" in value:
        out["LoggingLevel"] = value["logging_level"]
    if "data_trace_enabled" in value:
        out["DataTraceEnabled"] = value["data_trace_enabled"]
    if "throttling_burst_limit" in value:
        out["ThrottlingBurstLimit"] = value["throttling_burst_limit"]
    if "throttling_rate_limit" in value:
        out["ThrottlingRateLimit"] = value["throttling_rate_limit"]
    if "caching_enabled" in value:
        out["CachingEnabled"] = value["caching_enabled"]
    if "cache_ttl_in_seconds" in value:
        out["CacheTtlInSeconds"] = value["cache_ttl_in_seconds"]
    if "cache_data_encrypted" in value:
        out["CacheDataEncrypted"] = value["cache_data_encrypted"]
    if "require_authorization_for_cache_control" in value:
        out["RequireAuthorizationForCacheControl"] = value[
            "require_authorization_for_cache_control"
        ]
    if "unauthorized_cache_control_header_strategy" in value:
        out["UnauthorizedCacheControlHeaderStrategy"] = value[
            "unauthorized_cache_control_header_strategy"
        ]
    if "http_method" in value:
        out["HttpMethod"] = value["http_method"]
    if "resource_path" in value:
        out["ResourcePath"] = value["resource_path"]
    return out


def deserialize_json(data: dict) -> AwsApiGatewayMethodSettings:
    out: AwsApiGatewayMethodSettings = {}  # type: ignore[typeddict-item]
    if "MetricsEnabled" in data:
        out["metrics_enabled"] = data["MetricsEnabled"]
    if "LoggingLevel" in data:
        out["logging_level"] = data["LoggingLevel"]
    if "DataTraceEnabled" in data:
        out["data_trace_enabled"] = data["DataTraceEnabled"]
    if "ThrottlingBurstLimit" in data:
        out["throttling_burst_limit"] = data["ThrottlingBurstLimit"]
    if "ThrottlingRateLimit" in data:
        out["throttling_rate_limit"] = data["ThrottlingRateLimit"]
    if "CachingEnabled" in data:
        out["caching_enabled"] = data["CachingEnabled"]
    if "CacheTtlInSeconds" in data:
        out["cache_ttl_in_seconds"] = data["CacheTtlInSeconds"]
    if "CacheDataEncrypted" in data:
        out["cache_data_encrypted"] = data["CacheDataEncrypted"]
    if "RequireAuthorizationForCacheControl" in data:
        out["require_authorization_for_cache_control"] = data[
            "RequireAuthorizationForCacheControl"
        ]
    if "UnauthorizedCacheControlHeaderStrategy" in data:
        out["unauthorized_cache_control_header_strategy"] = data[
            "UnauthorizedCacheControlHeaderStrategy"
        ]
    if "HttpMethod" in data:
        out["http_method"] = data["HttpMethod"]
    if "ResourcePath" in data:
        out["resource_path"] = data["ResourcePath"]
    return out
