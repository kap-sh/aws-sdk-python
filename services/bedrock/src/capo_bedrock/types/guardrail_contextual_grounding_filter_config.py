"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingFilterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_contextual_grounding_action
    import capo_bedrock.types.guardrail_contextual_grounding_filter_type


class GuardrailContextualGroundingFilterConfig(TypedDict, closed=True):
    type: "capo_bedrock.types.guardrail_contextual_grounding_filter_type.GuardrailContextualGroundingFilterType"
    """<p>The filter details for the guardrails contextual grounding filter.</p>"""
    threshold: "float"
    """<p>The threshold details for the guardrails contextual grounding filter.</p>"""
    action: NotRequired[
        "capo_bedrock.types.guardrail_contextual_grounding_action.GuardrailContextualGroundingAction"
    ]
    """<p>Specifies the action to take when content fails the contextual grounding evaluation. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    enabled: NotRequired["bool"]
    """<p>Specifies whether to enable contextual grounding evaluation. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingFilterConfig) -> dict:
    out: dict = {}
    import capo_bedrock.types.guardrail_contextual_grounding_filter_type

    out["type"] = (
        capo_bedrock.types.guardrail_contextual_grounding_filter_type.serialize_json(
            value["type"]
        )
    )
    out["threshold"] = value["threshold"]
    if "action" in value:
        import capo_bedrock.types.guardrail_contextual_grounding_action

        out["action"] = (
            capo_bedrock.types.guardrail_contextual_grounding_action.serialize_json(
                value["action"]
            )
        )
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> GuardrailContextualGroundingFilterConfig:
    out: GuardrailContextualGroundingFilterConfig = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_bedrock.types.guardrail_contextual_grounding_filter_type

        out["type"] = (
            capo_bedrock.types.guardrail_contextual_grounding_filter_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError(
            "GuardrailContextualGroundingFilterConfig.type required"
        )
    if "threshold" in data:
        out["threshold"] = data["threshold"]
    else:
        raise DeserializationError(
            "GuardrailContextualGroundingFilterConfig.threshold required"
        )
    if "action" in data:
        import capo_bedrock.types.guardrail_contextual_grounding_action

        out["action"] = (
            capo_bedrock.types.guardrail_contextual_grounding_action.deserialize_json(
                data["action"]
            )
        )
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
