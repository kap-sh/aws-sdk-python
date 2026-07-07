"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContentPolicyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_content_filters_config
    import aws_sdk_bedrock.types.guardrail_content_filters_tier_config


class GuardrailContentPolicyConfig(TypedDict, closed=True):
    filters_config: "aws_sdk_bedrock.types.guardrail_content_filters_config.GuardrailContentFiltersConfig"
    """<p>Contains the type of the content filter and how strongly it should apply to prompts and model responses.</p>"""
    tier_config: NotRequired[
        "aws_sdk_bedrock.types.guardrail_content_filters_tier_config.GuardrailContentFiltersTierConfig"
    ]
    """<p>The tier that your guardrail uses for content filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentPolicyConfig) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.guardrail_content_filters_config

    out["filtersConfig"] = (
        aws_sdk_bedrock.types.guardrail_content_filters_config.serialize_json(
            value["filters_config"]
        )
    )
    if "tier_config" in value:
        import aws_sdk_bedrock.types.guardrail_content_filters_tier_config

        out["tierConfig"] = (
            aws_sdk_bedrock.types.guardrail_content_filters_tier_config.serialize_json(
                value["tier_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailContentPolicyConfig:
    out: GuardrailContentPolicyConfig = {}  # type: ignore[typeddict-item]
    if "filtersConfig" in data:
        import aws_sdk_bedrock.types.guardrail_content_filters_config

        out["filters_config"] = (
            aws_sdk_bedrock.types.guardrail_content_filters_config.deserialize_json(
                data["filtersConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GuardrailContentPolicyConfig.filters_config required"
        )
    if "tierConfig" in data:
        import aws_sdk_bedrock.types.guardrail_content_filters_tier_config

        out["tier_config"] = (
            aws_sdk_bedrock.types.guardrail_content_filters_tier_config.deserialize_json(
                data["tierConfig"]
            )
        )
    return out
