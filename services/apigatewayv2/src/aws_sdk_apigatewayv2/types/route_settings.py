"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RouteSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__boolean
    import aws_sdk_apigatewayv2.types.__double
    import aws_sdk_apigatewayv2.types.__integer
    import aws_sdk_apigatewayv2.types.logging_level


class RouteSettings(TypedDict):
    data_trace_enabled: NotRequired["aws_sdk_apigatewayv2.types.__boolean.__boolean"]
    """<p>Specifies whether (true) or not (false) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.</p>"""
    detailed_metrics_enabled: NotRequired[
        "aws_sdk_apigatewayv2.types.__boolean.__boolean"
    ]
    """<p>Specifies whether detailed metrics are enabled.</p>"""
    logging_level: NotRequired["aws_sdk_apigatewayv2.types.logging_level.LoggingLevel"]
    """<p>Specifies the logging level for this route: INFO, ERROR, or OFF. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.</p>"""
    throttling_burst_limit: NotRequired[
        "aws_sdk_apigatewayv2.types.__integer.__integer"
    ]
    """<p>Specifies the throttling burst limit.</p>"""
    throttling_rate_limit: NotRequired["aws_sdk_apigatewayv2.types.__double.__double"]
    """<p>Specifies the throttling rate limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteSettings) -> dict:
    out: dict = {}
    if "data_trace_enabled" in value:
        out["dataTraceEnabled"] = value["data_trace_enabled"]
    if "detailed_metrics_enabled" in value:
        out["detailedMetricsEnabled"] = value["detailed_metrics_enabled"]
    if "logging_level" in value:
        import aws_sdk_apigatewayv2.types.logging_level

        out["loggingLevel"] = aws_sdk_apigatewayv2.types.logging_level.serialize_json(
            value["logging_level"]
        )
    if "throttling_burst_limit" in value:
        out["throttlingBurstLimit"] = value["throttling_burst_limit"]
    if "throttling_rate_limit" in value:
        out["throttlingRateLimit"] = value["throttling_rate_limit"]
    return out


def deserialize_json(data: dict) -> RouteSettings:
    out: RouteSettings = {}  # type: ignore[typeddict-item]
    if "dataTraceEnabled" in data:
        out["data_trace_enabled"] = data["dataTraceEnabled"]
    if "detailedMetricsEnabled" in data:
        out["detailed_metrics_enabled"] = data["detailedMetricsEnabled"]
    if "loggingLevel" in data:
        import aws_sdk_apigatewayv2.types.logging_level

        out["logging_level"] = (
            aws_sdk_apigatewayv2.types.logging_level.deserialize_json(
                data["loggingLevel"]
            )
        )
    if "throttlingBurstLimit" in data:
        out["throttling_burst_limit"] = data["throttlingBurstLimit"]
    if "throttlingRateLimit" in data:
        out["throttling_rate_limit"] = data["throttlingRateLimit"]
    return out
