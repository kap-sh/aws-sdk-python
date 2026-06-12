"""Generated from Smithy shape ``com.amazonaws.apigateway#MethodSetting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.boolean
    import aws_sdk_api_gateway.types.double
    import aws_sdk_api_gateway.types.integer
    import aws_sdk_api_gateway.types.string
    import aws_sdk_api_gateway.types.unauthorized_cache_control_header_strategy


class MethodSetting(TypedDict):
    metrics_enabled: "aws_sdk_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether Amazon CloudWatch metrics are enabled for this method.</p>"""
    logging_level: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>Specifies the logging level for this method, which affects the log entries pushed to Amazon CloudWatch Logs. Valid values are <code>OFF</code>, <code>ERROR</code>, and <code>INFO</code>. Choose <code>ERROR</code> to write only error-level entries to CloudWatch Logs, or choose <code>INFO</code> to include all <code>ERROR</code> events as well as extra informational events.</p>"""
    data_trace_enabled: "aws_sdk_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether data trace logging is enabled for this method, which affects the log entries pushed to Amazon CloudWatch Logs. This can be useful to troubleshoot APIs, but can result in logging sensitive data. We recommend that you don't enable this option for production APIs.</p>"""
    throttling_burst_limit: "aws_sdk_api_gateway.types.integer.Integer"
    """<p>Specifies the throttling burst limit.</p>"""
    throttling_rate_limit: "aws_sdk_api_gateway.types.double.Double"
    """<p>Specifies the throttling rate limit.</p>"""
    caching_enabled: "aws_sdk_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether responses should be cached and returned for requests. A cache cluster must be enabled on the stage for responses to be cached.</p>"""
    cache_ttl_in_seconds: "aws_sdk_api_gateway.types.integer.Integer"
    """<p>Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL, the longer the response will be cached.</p>"""
    cache_data_encrypted: "aws_sdk_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether the cached responses are encrypted.</p>"""
    require_authorization_for_cache_control: "aws_sdk_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether authorization is required for a cache invalidation request.</p>"""
    unauthorized_cache_control_header_strategy: NotRequired[
        "aws_sdk_api_gateway.types.unauthorized_cache_control_header_strategy.UnauthorizedCacheControlHeaderStrategy"
    ]
    """<p>Specifies how to handle unauthorized requests for cache invalidation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MethodSetting) -> dict:
    out: dict = {}
    out["metricsEnabled"] = value.get("metrics_enabled", False)
    if "logging_level" in value:
        out["loggingLevel"] = value["logging_level"]
    out["dataTraceEnabled"] = value.get("data_trace_enabled", False)
    out["throttlingBurstLimit"] = value.get("throttling_burst_limit", 0)
    out["throttlingRateLimit"] = value.get("throttling_rate_limit", 0)
    out["cachingEnabled"] = value.get("caching_enabled", False)
    out["cacheTtlInSeconds"] = value.get("cache_ttl_in_seconds", 0)
    out["cacheDataEncrypted"] = value.get("cache_data_encrypted", False)
    out["requireAuthorizationForCacheControl"] = value.get(
        "require_authorization_for_cache_control", False
    )
    if "unauthorized_cache_control_header_strategy" in value:
        import aws_sdk_api_gateway.types.unauthorized_cache_control_header_strategy

        out["unauthorizedCacheControlHeaderStrategy"] = (
            aws_sdk_api_gateway.types.unauthorized_cache_control_header_strategy.serialize_json(
                value["unauthorized_cache_control_header_strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> MethodSetting:
    out: MethodSetting = {}  # type: ignore[typeddict-item]
    if "metricsEnabled" in data:
        out["metrics_enabled"] = data["metricsEnabled"]
    else:
        out["metrics_enabled"] = False
    if "loggingLevel" in data:
        out["logging_level"] = data["loggingLevel"]
    if "dataTraceEnabled" in data:
        out["data_trace_enabled"] = data["dataTraceEnabled"]
    else:
        out["data_trace_enabled"] = False
    if "throttlingBurstLimit" in data:
        out["throttling_burst_limit"] = data["throttlingBurstLimit"]
    else:
        out["throttling_burst_limit"] = 0
    if "throttlingRateLimit" in data:
        out["throttling_rate_limit"] = data["throttlingRateLimit"]
    else:
        out["throttling_rate_limit"] = 0
    if "cachingEnabled" in data:
        out["caching_enabled"] = data["cachingEnabled"]
    else:
        out["caching_enabled"] = False
    if "cacheTtlInSeconds" in data:
        out["cache_ttl_in_seconds"] = data["cacheTtlInSeconds"]
    else:
        out["cache_ttl_in_seconds"] = 0
    if "cacheDataEncrypted" in data:
        out["cache_data_encrypted"] = data["cacheDataEncrypted"]
    else:
        out["cache_data_encrypted"] = False
    if "requireAuthorizationForCacheControl" in data:
        out["require_authorization_for_cache_control"] = data[
            "requireAuthorizationForCacheControl"
        ]
    else:
        out["require_authorization_for_cache_control"] = False
    if "unauthorizedCacheControlHeaderStrategy" in data:
        import aws_sdk_api_gateway.types.unauthorized_cache_control_header_strategy

        out["unauthorized_cache_control_header_strategy"] = (
            aws_sdk_api_gateway.types.unauthorized_cache_control_header_strategy.deserialize_json(
                data["unauthorizedCacheControlHeaderStrategy"]
            )
        )
    return out
