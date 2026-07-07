"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContextualGroundingPolicyAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_contextual_grounding_filters


class GuardrailContextualGroundingPolicyAssessment(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_contextual_grounding_filters.GuardrailContextualGroundingFilters"
    ]
    """<p>The filter details for the guardrails contextual grounding filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingPolicyAssessment) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_contextual_grounding_filters

        out["filters"] = (
            aws_sdk_bedrock_runtime.types.guardrail_contextual_grounding_filters.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailContextualGroundingPolicyAssessment:
    out: GuardrailContextualGroundingPolicyAssessment = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_contextual_grounding_filters

        out["filters"] = (
            aws_sdk_bedrock_runtime.types.guardrail_contextual_grounding_filters.deserialize_json(
                data["filters"]
            )
        )
    return out
