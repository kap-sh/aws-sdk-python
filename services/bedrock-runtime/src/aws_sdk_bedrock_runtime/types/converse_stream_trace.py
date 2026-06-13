"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseStreamTrace``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_trace_assessment
    import aws_sdk_bedrock_runtime.types.prompt_router_trace


class ConverseStreamTrace(TypedDict):
    guardrail: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_trace_assessment.GuardrailTraceAssessment"
    ]
    """<p>The guardrail trace object. </p>"""
    prompt_router: NotRequired[
        "aws_sdk_bedrock_runtime.types.prompt_router_trace.PromptRouterTrace"
    ]
    """<p>The request's prompt router.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConverseStreamTrace) -> dict:
    out: dict = {}
    if "guardrail" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_trace_assessment

        out["guardrail"] = (
            aws_sdk_bedrock_runtime.types.guardrail_trace_assessment.serialize_json(
                value["guardrail"]
            )
        )
    if "prompt_router" in value:
        import aws_sdk_bedrock_runtime.types.prompt_router_trace

        out["promptRouter"] = (
            aws_sdk_bedrock_runtime.types.prompt_router_trace.serialize_json(
                value["prompt_router"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConverseStreamTrace:
    out: ConverseStreamTrace = {}  # type: ignore[typeddict-item]
    if "guardrail" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_trace_assessment

        out["guardrail"] = (
            aws_sdk_bedrock_runtime.types.guardrail_trace_assessment.deserialize_json(
                data["guardrail"]
            )
        )
    if "promptRouter" in data:
        import aws_sdk_bedrock_runtime.types.prompt_router_trace

        out["prompt_router"] = (
            aws_sdk_bedrock_runtime.types.prompt_router_trace.deserialize_json(
                data["promptRouter"]
            )
        )
    return out
