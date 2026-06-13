"""Generated from Smithy shape ``com.amazonaws.qconnect#GetAIGuardrailResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_guardrail_data
    import aws_sdk_qconnect.types.version


class GetAIGuardrailResponse(TypedDict):
    ai_guardrail: NotRequired[
        "aws_sdk_qconnect.types.ai_guardrail_data.AIGuardrailData"
    ]
    """<p>The data of the AI Guardrail.</p>"""
    version_number: NotRequired["aws_sdk_qconnect.types.version.Version"]
    """<p>The version number of the AI Guardrail version (returned if an AI Guardrail version was specified via use of a qualifier for the <code>aiGuardrailId</code> on the request). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAIGuardrailResponse) -> dict:
    out: dict = {}
    if "ai_guardrail" in value:
        import aws_sdk_qconnect.types.ai_guardrail_data

        out["aiGuardrail"] = aws_sdk_qconnect.types.ai_guardrail_data.serialize_json(
            value["ai_guardrail"]
        )
    if "version_number" in value:
        out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> GetAIGuardrailResponse:
    out: GetAIGuardrailResponse = {}  # type: ignore[typeddict-item]
    if "aiGuardrail" in data:
        import aws_sdk_qconnect.types.ai_guardrail_data

        out["ai_guardrail"] = aws_sdk_qconnect.types.ai_guardrail_data.deserialize_json(
            data["aiGuardrail"]
        )
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    return out
