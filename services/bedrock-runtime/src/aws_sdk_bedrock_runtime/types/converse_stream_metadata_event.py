"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseStreamMetadataEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime._protocol.eventstream import HeaderValue, Message
from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.converse_stream_metrics
    import aws_sdk_bedrock_runtime.types.converse_stream_trace
    import aws_sdk_bedrock_runtime.types.performance_configuration
    import aws_sdk_bedrock_runtime.types.service_tier
    import aws_sdk_bedrock_runtime.types.token_usage


class ConverseStreamMetadataEvent(TypedDict, closed=True):
    usage: "aws_sdk_bedrock_runtime.types.token_usage.TokenUsage"
    """<p>Usage information for the conversation stream event.</p>"""
    metrics: (
        "aws_sdk_bedrock_runtime.types.converse_stream_metrics.ConverseStreamMetrics"
    )
    """<p>The metrics for the conversation stream metadata event.</p>"""
    trace: NotRequired[
        "aws_sdk_bedrock_runtime.types.converse_stream_trace.ConverseStreamTrace"
    ]
    r"""<p>The trace object in the response from <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html\">ConverseStream</a> that contains information about the guardrail behavior.</p>"""
    performance_config: NotRequired[
        "aws_sdk_bedrock_runtime.types.performance_configuration.PerformanceConfiguration"
    ]
    """<p>Model performance configuration metadata for the conversation stream event.</p>"""
    service_tier: NotRequired["aws_sdk_bedrock_runtime.types.service_tier.ServiceTier"]
    """<p>Specifies the processing tier configuration used for serving the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConverseStreamMetadataEvent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.token_usage

    out["usage"] = aws_sdk_bedrock_runtime.types.token_usage.serialize_json(
        value["usage"]
    )
    import aws_sdk_bedrock_runtime.types.converse_stream_metrics

    out["metrics"] = (
        aws_sdk_bedrock_runtime.types.converse_stream_metrics.serialize_json(
            value["metrics"]
        )
    )
    if "trace" in value:
        import aws_sdk_bedrock_runtime.types.converse_stream_trace

        out["trace"] = (
            aws_sdk_bedrock_runtime.types.converse_stream_trace.serialize_json(
                value["trace"]
            )
        )
    if "performance_config" in value:
        import aws_sdk_bedrock_runtime.types.performance_configuration

        out["performanceConfig"] = (
            aws_sdk_bedrock_runtime.types.performance_configuration.serialize_json(
                value["performance_config"]
            )
        )
    if "service_tier" in value:
        import aws_sdk_bedrock_runtime.types.service_tier

        out["serviceTier"] = aws_sdk_bedrock_runtime.types.service_tier.serialize_json(
            value["service_tier"]
        )
    return out


def deserialize_json(data: dict) -> ConverseStreamMetadataEvent:
    out: ConverseStreamMetadataEvent = {}  # type: ignore[typeddict-item]
    if "usage" in data:
        import aws_sdk_bedrock_runtime.types.token_usage

        out["usage"] = aws_sdk_bedrock_runtime.types.token_usage.deserialize_json(
            data["usage"]
        )
    else:
        raise DeserializationError("ConverseStreamMetadataEvent.usage required")
    if "metrics" in data:
        import aws_sdk_bedrock_runtime.types.converse_stream_metrics

        out["metrics"] = (
            aws_sdk_bedrock_runtime.types.converse_stream_metrics.deserialize_json(
                data["metrics"]
            )
        )
    else:
        raise DeserializationError("ConverseStreamMetadataEvent.metrics required")
    if "trace" in data:
        import aws_sdk_bedrock_runtime.types.converse_stream_trace

        out["trace"] = (
            aws_sdk_bedrock_runtime.types.converse_stream_trace.deserialize_json(
                data["trace"]
            )
        )
    if "performanceConfig" in data:
        import aws_sdk_bedrock_runtime.types.performance_configuration

        out["performance_config"] = (
            aws_sdk_bedrock_runtime.types.performance_configuration.deserialize_json(
                data["performanceConfig"]
            )
        )
    if "serviceTier" in data:
        import aws_sdk_bedrock_runtime.types.service_tier

        out["service_tier"] = (
            aws_sdk_bedrock_runtime.types.service_tier.deserialize_json(
                data["serviceTier"]
            )
        )
    return out


def serialize_event_json(value: ConverseStreamMetadataEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "metadata"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ConverseStreamMetadataEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ConverseStreamMetadataEvent = {}  # type: ignore[typeddict-item]
    return out
