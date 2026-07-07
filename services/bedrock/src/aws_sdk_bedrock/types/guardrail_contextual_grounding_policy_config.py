"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingPolicyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_contextual_grounding_filters_config


class GuardrailContextualGroundingPolicyConfig(TypedDict, closed=True):
    filters_config: "aws_sdk_bedrock.types.guardrail_contextual_grounding_filters_config.GuardrailContextualGroundingFiltersConfig"
    """<p>The filter configuration details for the guardrails contextual grounding policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingPolicyConfig) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.guardrail_contextual_grounding_filters_config

    out["filtersConfig"] = (
        aws_sdk_bedrock.types.guardrail_contextual_grounding_filters_config.serialize_json(
            value["filters_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailContextualGroundingPolicyConfig:
    out: GuardrailContextualGroundingPolicyConfig = {}  # type: ignore[typeddict-item]
    if "filtersConfig" in data:
        import aws_sdk_bedrock.types.guardrail_contextual_grounding_filters_config

        out["filters_config"] = (
            aws_sdk_bedrock.types.guardrail_contextual_grounding_filters_config.deserialize_json(
                data["filtersConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GuardrailContextualGroundingPolicyConfig.filters_config required"
        )
    return out
