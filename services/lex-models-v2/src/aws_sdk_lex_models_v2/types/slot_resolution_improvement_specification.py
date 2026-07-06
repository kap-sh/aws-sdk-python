"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotResolutionImprovementSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bedrock_model_specification
    import aws_sdk_lex_models_v2.types.enabled


class SlotResolutionImprovementSpecification(TypedDict, closed=True):
    enabled: "aws_sdk_lex_models_v2.types.enabled.Enabled"
    """<p>Specifies whether assisted slot resolution is turned on or off.</p>"""
    bedrock_model_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.bedrock_model_specification.BedrockModelSpecification"
    ]
    """<p>An object containing information about the Amazon Bedrock model used to assist slot resolution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotResolutionImprovementSpecification) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "bedrock_model_specification" in value:
        import aws_sdk_lex_models_v2.types.bedrock_model_specification

        out["bedrockModelSpecification"] = (
            aws_sdk_lex_models_v2.types.bedrock_model_specification.serialize_json(
                value["bedrock_model_specification"]
            )
        )
    return out


def deserialize_json(data: dict) -> SlotResolutionImprovementSpecification:
    out: SlotResolutionImprovementSpecification = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "bedrockModelSpecification" in data:
        import aws_sdk_lex_models_v2.types.bedrock_model_specification

        out["bedrock_model_specification"] = (
            aws_sdk_lex_models_v2.types.bedrock_model_specification.deserialize_json(
                data["bedrockModelSpecification"]
            )
        )
    return out
