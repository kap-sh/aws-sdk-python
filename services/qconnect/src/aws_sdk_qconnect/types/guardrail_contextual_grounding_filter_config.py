"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailContextualGroundingFilterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.guardrail_contextual_grounding_filter_threshold
    import aws_sdk_qconnect.types.guardrail_contextual_grounding_filter_type


class GuardrailContextualGroundingFilterConfig(TypedDict, closed=True):
    type: "aws_sdk_qconnect.types.guardrail_contextual_grounding_filter_type.GuardrailContextualGroundingFilterType"
    """<p>The filter type for the AI Guardrail's contextual grounding filter.</p>"""
    threshold: "aws_sdk_qconnect.types.guardrail_contextual_grounding_filter_threshold.GuardrailContextualGroundingFilterThreshold"
    """<p>The threshold details for the AI Guardrail's contextual grounding filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingFilterConfig) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["threshold"] = value.get("threshold", 0)
    return out


def deserialize_json(data: dict) -> GuardrailContextualGroundingFilterConfig:
    out: GuardrailContextualGroundingFilterConfig = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError(
            "GuardrailContextualGroundingFilterConfig.type required"
        )
    if "threshold" in data:
        out["threshold"] = data["threshold"]
    else:
        out["threshold"] = 0
    return out
