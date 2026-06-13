"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailInvocationMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_coverage
    import aws_sdk_bedrock_runtime.types.guardrail_processing_latency
    import aws_sdk_bedrock_runtime.types.guardrail_usage


class GuardrailInvocationMetrics(TypedDict):
    guardrail_processing_latency: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_processing_latency.GuardrailProcessingLatency"
    ]
    """<p>The processing latency details for the guardrail invocation metrics.</p>"""
    usage: NotRequired["aws_sdk_bedrock_runtime.types.guardrail_usage.GuardrailUsage"]
    """<p>The usage details for the guardrail invocation metrics.</p>"""
    guardrail_coverage: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_coverage.GuardrailCoverage"
    ]
    """<p>The coverage details for the guardrail invocation metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailInvocationMetrics) -> dict:
    out: dict = {}
    if "guardrail_processing_latency" in value:
        out["guardrailProcessingLatency"] = value["guardrail_processing_latency"]
    if "usage" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_usage

        out["usage"] = aws_sdk_bedrock_runtime.types.guardrail_usage.serialize_json(
            value["usage"]
        )
    if "guardrail_coverage" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_coverage

        out["guardrailCoverage"] = (
            aws_sdk_bedrock_runtime.types.guardrail_coverage.serialize_json(
                value["guardrail_coverage"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailInvocationMetrics:
    out: GuardrailInvocationMetrics = {}  # type: ignore[typeddict-item]
    if "guardrailProcessingLatency" in data:
        out["guardrail_processing_latency"] = data["guardrailProcessingLatency"]
    if "usage" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_usage

        out["usage"] = aws_sdk_bedrock_runtime.types.guardrail_usage.deserialize_json(
            data["usage"]
        )
    if "guardrailCoverage" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_coverage

        out["guardrail_coverage"] = (
            aws_sdk_bedrock_runtime.types.guardrail_coverage.deserialize_json(
                data["guardrailCoverage"]
            )
        )
    return out
