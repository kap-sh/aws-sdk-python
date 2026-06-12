"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingPolicy``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_contextual_grounding_filters


class GuardrailContextualGroundingPolicy(TypedDict):
    filters: "aws_sdk_bedrock.types.guardrail_contextual_grounding_filters.GuardrailContextualGroundingFilters"
    """<p>The filter details for the guardrails contextual grounding policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingPolicy) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.guardrail_contextual_grounding_filters

    out["filters"] = (
        aws_sdk_bedrock.types.guardrail_contextual_grounding_filters.serialize_json(
            value["filters"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailContextualGroundingPolicy:
    out: GuardrailContextualGroundingPolicy = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_bedrock.types.guardrail_contextual_grounding_filters

        out["filters"] = (
            aws_sdk_bedrock.types.guardrail_contextual_grounding_filters.deserialize_json(
                data["filters"]
            )
        )
    else:
        raise DeserializationError(
            "GuardrailContextualGroundingPolicy.filters required"
        )
    return out
