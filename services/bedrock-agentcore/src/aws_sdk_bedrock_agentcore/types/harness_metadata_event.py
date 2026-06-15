"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessMetadataEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_stream_metrics
    import aws_sdk_bedrock_agentcore.types.harness_token_usage


class HarnessMetadataEvent(TypedDict):
    usage: "aws_sdk_bedrock_agentcore.types.harness_token_usage.HarnessTokenUsage"
    """<p>Token usage counts.</p>"""
    metrics: (
        "aws_sdk_bedrock_agentcore.types.harness_stream_metrics.HarnessStreamMetrics"
    )
    """<p>Latency metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessMetadataEvent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.harness_token_usage

    out["usage"] = aws_sdk_bedrock_agentcore.types.harness_token_usage.serialize_json(
        value["usage"]
    )
    import aws_sdk_bedrock_agentcore.types.harness_stream_metrics

    out["metrics"] = (
        aws_sdk_bedrock_agentcore.types.harness_stream_metrics.serialize_json(
            value["metrics"]
        )
    )
    return out


def deserialize_json(data: dict) -> HarnessMetadataEvent:
    out: HarnessMetadataEvent = {}  # type: ignore[typeddict-item]
    if "usage" in data:
        import aws_sdk_bedrock_agentcore.types.harness_token_usage

        out["usage"] = (
            aws_sdk_bedrock_agentcore.types.harness_token_usage.deserialize_json(
                data["usage"]
            )
        )
    else:
        raise DeserializationError("HarnessMetadataEvent.usage required")
    if "metrics" in data:
        import aws_sdk_bedrock_agentcore.types.harness_stream_metrics

        out["metrics"] = (
            aws_sdk_bedrock_agentcore.types.harness_stream_metrics.deserialize_json(
                data["metrics"]
            )
        )
    else:
        raise DeserializationError("HarnessMetadataEvent.metrics required")
    return out
