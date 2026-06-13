"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_contextual_grounding_action
    import aws_sdk_bedrock.types.guardrail_contextual_grounding_filter_type


class GuardrailContextualGroundingFilter(TypedDict):
    type: "aws_sdk_bedrock.types.guardrail_contextual_grounding_filter_type.GuardrailContextualGroundingFilterType"
    """<p>The filter type details for the guardrails contextual grounding filter.</p>"""
    threshold: "float"
    """<p>The threshold details for the guardrails contextual grounding filter.</p>"""
    action: NotRequired[
        "aws_sdk_bedrock.types.guardrail_contextual_grounding_action.GuardrailContextualGroundingAction"
    ]
    """<p>The action to take when content fails the contextual grounding evaluation. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    enabled: NotRequired["bool"]
    """<p>Indicates whether contextual grounding is enabled for evaluation. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingFilter) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.guardrail_contextual_grounding_filter_type

    out["type"] = (
        aws_sdk_bedrock.types.guardrail_contextual_grounding_filter_type.serialize_json(
            value["type"]
        )
    )
    out["threshold"] = value["threshold"]
    if "action" in value:
        import aws_sdk_bedrock.types.guardrail_contextual_grounding_action

        out["action"] = (
            aws_sdk_bedrock.types.guardrail_contextual_grounding_action.serialize_json(
                value["action"]
            )
        )
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> GuardrailContextualGroundingFilter:
    out: GuardrailContextualGroundingFilter = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock.types.guardrail_contextual_grounding_filter_type

        out["type"] = (
            aws_sdk_bedrock.types.guardrail_contextual_grounding_filter_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("GuardrailContextualGroundingFilter.type required")
    if "threshold" in data:
        out["threshold"] = data["threshold"]
    else:
        raise DeserializationError(
            "GuardrailContextualGroundingFilter.threshold required"
        )
    if "action" in data:
        import aws_sdk_bedrock.types.guardrail_contextual_grounding_action

        out["action"] = (
            aws_sdk_bedrock.types.guardrail_contextual_grounding_action.deserialize_json(
                data["action"]
            )
        )
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
