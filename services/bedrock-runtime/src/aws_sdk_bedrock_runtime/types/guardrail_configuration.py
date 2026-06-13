"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_identifier
    import aws_sdk_bedrock_runtime.types.guardrail_trace
    import aws_sdk_bedrock_runtime.types.guardrail_version


class GuardrailConfiguration(TypedDict):
    guardrail_identifier: (
        "aws_sdk_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier"
    )
    """<p>The identifier for the guardrail.</p>"""
    guardrail_version: (
        "aws_sdk_bedrock_runtime.types.guardrail_version.GuardrailVersion"
    )
    """<p>The version of the guardrail.</p>"""
    trace: "aws_sdk_bedrock_runtime.types.guardrail_trace.GuardrailTrace"
    """<p>The trace behavior for the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConfiguration) -> dict:
    out: dict = {}
    out["guardrailIdentifier"] = value.get("guardrail_identifier", "")
    out["guardrailVersion"] = value.get("guardrail_version", "")
    import aws_sdk_bedrock_runtime.types.guardrail_trace

    out["trace"] = aws_sdk_bedrock_runtime.types.guardrail_trace.serialize_json(
        value.get("trace", "disabled")
    )
    return out


def deserialize_json(data: dict) -> GuardrailConfiguration:
    out: GuardrailConfiguration = {}  # type: ignore[typeddict-item]
    if "guardrailIdentifier" in data:
        out["guardrail_identifier"] = data["guardrailIdentifier"]
    else:
        out["guardrail_identifier"] = ""
    if "guardrailVersion" in data:
        out["guardrail_version"] = data["guardrailVersion"]
    else:
        out["guardrail_version"] = ""
    if "trace" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_trace

        out["trace"] = aws_sdk_bedrock_runtime.types.guardrail_trace.deserialize_json(
            data["trace"]
        )
    else:
        out["trace"] = "disabled"
    return out
