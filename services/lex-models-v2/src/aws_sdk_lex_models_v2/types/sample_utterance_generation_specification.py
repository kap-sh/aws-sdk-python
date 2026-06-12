"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SampleUtteranceGenerationSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bedrock_model_specification
    import aws_sdk_lex_models_v2.types.boolean


class SampleUtteranceGenerationSpecification(TypedDict):
    enabled: "aws_sdk_lex_models_v2.types.boolean.Boolean"
    """<p>Specifies whether to enable sample utterance generation or not.</p>"""
    bedrock_model_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.bedrock_model_specification.BedrockModelSpecification"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SampleUtteranceGenerationSpecification) -> dict:
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


def deserialize_json(data: dict) -> SampleUtteranceGenerationSpecification:
    out: SampleUtteranceGenerationSpecification = {}  # type: ignore[typeddict-item]
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
