"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailStreamConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_identifier
    import aws_sdk_bedrock_runtime.types.guardrail_stream_processing_mode
    import aws_sdk_bedrock_runtime.types.guardrail_trace
    import aws_sdk_bedrock_runtime.types.guardrail_version


class GuardrailStreamConfiguration(TypedDict, closed=True):
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
    stream_processing_mode: "aws_sdk_bedrock_runtime.types.guardrail_stream_processing_mode.GuardrailStreamProcessingMode"
    """<p>The processing mode. </p> <p>The processing mode. For more information, see <i>Configure streaming response behavior</i> in the <i>Amazon Bedrock User Guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailStreamConfiguration) -> dict:
    out: dict = {}
    out["guardrailIdentifier"] = value.get("guardrail_identifier", "")
    out["guardrailVersion"] = value.get("guardrail_version", "")
    import aws_sdk_bedrock_runtime.types.guardrail_trace

    out["trace"] = aws_sdk_bedrock_runtime.types.guardrail_trace.serialize_json(
        value.get("trace", "disabled")
    )
    import aws_sdk_bedrock_runtime.types.guardrail_stream_processing_mode

    out["streamProcessingMode"] = (
        aws_sdk_bedrock_runtime.types.guardrail_stream_processing_mode.serialize_json(
            value.get("stream_processing_mode", "sync")
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailStreamConfiguration:
    out: GuardrailStreamConfiguration = {}  # type: ignore[typeddict-item]
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
    if "streamProcessingMode" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_stream_processing_mode

        out["stream_processing_mode"] = (
            aws_sdk_bedrock_runtime.types.guardrail_stream_processing_mode.deserialize_json(
                data["streamProcessingMode"]
            )
        )
    else:
        out["stream_processing_mode"] = "sync"
    return out
