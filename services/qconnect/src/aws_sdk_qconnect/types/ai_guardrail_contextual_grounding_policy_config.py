"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailContextualGroundingPolicyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.guardrail_contextual_grounding_filters_config


class AIGuardrailContextualGroundingPolicyConfig(TypedDict, closed=True):
    filters_config: "aws_sdk_qconnect.types.guardrail_contextual_grounding_filters_config.GuardrailContextualGroundingFiltersConfig"
    """<p>The filter configuration details for the AI Guardrails contextual grounding policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailContextualGroundingPolicyConfig) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.guardrail_contextual_grounding_filters_config

    out["filtersConfig"] = (
        aws_sdk_qconnect.types.guardrail_contextual_grounding_filters_config.serialize_json(
            value["filters_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> AIGuardrailContextualGroundingPolicyConfig:
    out: AIGuardrailContextualGroundingPolicyConfig = {}  # type: ignore[typeddict-item]
    if "filtersConfig" in data:
        import aws_sdk_qconnect.types.guardrail_contextual_grounding_filters_config

        out["filters_config"] = (
            aws_sdk_qconnect.types.guardrail_contextual_grounding_filters_config.deserialize_json(
                data["filtersConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AIGuardrailContextualGroundingPolicyConfig.filters_config required"
        )
    return out
