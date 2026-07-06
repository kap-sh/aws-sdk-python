"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsApiGatewayV2RouteSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.double
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsApiGatewayV2RouteSettings(TypedDict, closed=True):
    detailed_metrics_enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether detailed metrics are enabled.</p>"""
    logging_level: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The logging level. The logging level affects the log entries that are pushed to CloudWatch Logs. Supported only for WebSocket APIs.</p> <p>If the logging level is <code>ERROR</code>, then the logs only include error-level entries.</p> <p>If the logging level is <code>INFO</code>, then the logs include both <code>ERROR</code> events and extra informational events.</p> <p>Valid values: <code>OFF</code> | <code>ERROR</code> | <code>INFO</code> </p>"""
    data_trace_enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether data trace logging is enabled. Data trace logging affects the log entries that are pushed to CloudWatch Logs. Supported only for WebSocket APIs.</p>"""
    throttling_burst_limit: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The throttling burst limit.</p>"""
    throttling_rate_limit: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p>The throttling rate limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiGatewayV2RouteSettings) -> dict:
    out: dict = {}
    if "detailed_metrics_enabled" in value:
        out["DetailedMetricsEnabled"] = value["detailed_metrics_enabled"]
    if "logging_level" in value:
        out["LoggingLevel"] = value["logging_level"]
    if "data_trace_enabled" in value:
        out["DataTraceEnabled"] = value["data_trace_enabled"]
    if "throttling_burst_limit" in value:
        out["ThrottlingBurstLimit"] = value["throttling_burst_limit"]
    if "throttling_rate_limit" in value:
        out["ThrottlingRateLimit"] = value["throttling_rate_limit"]
    return out


def deserialize_json(data: dict) -> AwsApiGatewayV2RouteSettings:
    out: AwsApiGatewayV2RouteSettings = {}  # type: ignore[typeddict-item]
    if "DetailedMetricsEnabled" in data:
        out["detailed_metrics_enabled"] = data["DetailedMetricsEnabled"]
    if "LoggingLevel" in data:
        out["logging_level"] = data["LoggingLevel"]
    if "DataTraceEnabled" in data:
        out["data_trace_enabled"] = data["DataTraceEnabled"]
    if "ThrottlingBurstLimit" in data:
        out["throttling_burst_limit"] = data["ThrottlingBurstLimit"]
    if "ThrottlingRateLimit" in data:
        out["throttling_rate_limit"] = data["ThrottlingRateLimit"]
    return out
