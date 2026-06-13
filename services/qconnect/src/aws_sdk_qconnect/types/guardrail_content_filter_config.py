"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailContentFilterConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.guardrail_content_filter_type
    import aws_sdk_qconnect.types.guardrail_filter_strength


class GuardrailContentFilterConfig(TypedDict):
    type: "aws_sdk_qconnect.types.guardrail_content_filter_type.GuardrailContentFilterType"
    """<p>The harmful category that the content filter is applied to.</p>"""
    input_strength: (
        "aws_sdk_qconnect.types.guardrail_filter_strength.GuardrailFilterStrength"
    )
    """<p>The strength of the content filter to apply to prompts. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.</p>"""
    output_strength: (
        "aws_sdk_qconnect.types.guardrail_filter_strength.GuardrailFilterStrength"
    )
    """<p>The strength of the content filter to apply to model responses. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFilterConfig) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["inputStrength"] = value["input_strength"]
    out["outputStrength"] = value["output_strength"]
    return out


def deserialize_json(data: dict) -> GuardrailContentFilterConfig:
    out: GuardrailContentFilterConfig = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("GuardrailContentFilterConfig.type required")
    if "inputStrength" in data:
        out["input_strength"] = data["inputStrength"]
    else:
        raise DeserializationError(
            "GuardrailContentFilterConfig.input_strength required"
        )
    if "outputStrength" in data:
        out["output_strength"] = data["outputStrength"]
    else:
        raise DeserializationError(
            "GuardrailContentFilterConfig.output_strength required"
        )
    return out
