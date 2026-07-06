"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContentPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_content_filters
    import aws_sdk_bedrock.types.guardrail_content_filters_tier


class GuardrailContentPolicy(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_bedrock.types.guardrail_content_filters.GuardrailContentFilters"
    ]
    """<p>Contains the type of the content filter and how strongly it should apply to prompts and model responses.</p>"""
    tier: NotRequired[
        "aws_sdk_bedrock.types.guardrail_content_filters_tier.GuardrailContentFiltersTier"
    ]
    """<p>The tier that your guardrail uses for content filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentPolicy) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_bedrock.types.guardrail_content_filters

        out["filters"] = aws_sdk_bedrock.types.guardrail_content_filters.serialize_json(
            value["filters"]
        )
    if "tier" in value:
        import aws_sdk_bedrock.types.guardrail_content_filters_tier

        out["tier"] = (
            aws_sdk_bedrock.types.guardrail_content_filters_tier.serialize_json(
                value["tier"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailContentPolicy:
    out: GuardrailContentPolicy = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_bedrock.types.guardrail_content_filters

        out["filters"] = (
            aws_sdk_bedrock.types.guardrail_content_filters.deserialize_json(
                data["filters"]
            )
        )
    if "tier" in data:
        import aws_sdk_bedrock.types.guardrail_content_filters_tier

        out["tier"] = (
            aws_sdk_bedrock.types.guardrail_content_filters_tier.deserialize_json(
                data["tier"]
            )
        )
    return out
