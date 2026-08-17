"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_identifier
    import capo_bedrock_runtime.types.guardrail_trace
    import capo_bedrock_runtime.types.guardrail_version


class GuardrailConfiguration(TypedDict, closed=True):
    guardrail_identifier: (
        "capo_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier"
    )
    """<p>The identifier for the guardrail.</p>"""
    guardrail_version: "capo_bedrock_runtime.types.guardrail_version.GuardrailVersion"
    """<p>The version of the guardrail.</p>"""
    trace: "capo_bedrock_runtime.types.guardrail_trace.GuardrailTrace"
    """<p>The trace behavior for the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConfiguration) -> dict:
    out: dict = {}
    out["guardrailIdentifier"] = value.get("guardrail_identifier", "")
    out["guardrailVersion"] = value.get("guardrail_version", "")
    import capo_bedrock_runtime.types.guardrail_trace

    out["trace"] = capo_bedrock_runtime.types.guardrail_trace.serialize_json(
        value.get("trace", "disabled")
    )
    return out


def deserialize_json(data: dict) -> GuardrailConfiguration:
    out: GuardrailConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("guardrailIdentifier") is not None:
        out["guardrail_identifier"] = data["guardrailIdentifier"]
    else:
        out["guardrail_identifier"] = ""
    if data.get("guardrailVersion") is not None:
        out["guardrail_version"] = data["guardrailVersion"]
    else:
        out["guardrail_version"] = ""
    if data.get("trace") is not None:
        import capo_bedrock_runtime.types.guardrail_trace

        out["trace"] = capo_bedrock_runtime.types.guardrail_trace.deserialize_json(
            data["trace"]
        )
    else:
        out["trace"] = "disabled"
    return out
