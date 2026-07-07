"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BuildtimeSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.descriptive_bot_builder_specification
    import aws_sdk_lex_models_v2.types.sample_utterance_generation_specification


class BuildtimeSettings(TypedDict, closed=True):
    descriptive_bot_builder: NotRequired[
        "aws_sdk_lex_models_v2.types.descriptive_bot_builder_specification.DescriptiveBotBuilderSpecification"
    ]
    """<p>An object containing specifications for the descriptive bot building feature.</p>"""
    sample_utterance_generation: NotRequired[
        "aws_sdk_lex_models_v2.types.sample_utterance_generation_specification.SampleUtteranceGenerationSpecification"
    ]
    """<p>Contains specifications for the sample utterance generation feature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BuildtimeSettings) -> dict:
    out: dict = {}
    if "descriptive_bot_builder" in value:
        import aws_sdk_lex_models_v2.types.descriptive_bot_builder_specification

        out["descriptiveBotBuilder"] = (
            aws_sdk_lex_models_v2.types.descriptive_bot_builder_specification.serialize_json(
                value["descriptive_bot_builder"]
            )
        )
    if "sample_utterance_generation" in value:
        import aws_sdk_lex_models_v2.types.sample_utterance_generation_specification

        out["sampleUtteranceGeneration"] = (
            aws_sdk_lex_models_v2.types.sample_utterance_generation_specification.serialize_json(
                value["sample_utterance_generation"]
            )
        )
    return out


def deserialize_json(data: dict) -> BuildtimeSettings:
    out: BuildtimeSettings = {}  # type: ignore[typeddict-item]
    if "descriptiveBotBuilder" in data:
        import aws_sdk_lex_models_v2.types.descriptive_bot_builder_specification

        out["descriptive_bot_builder"] = (
            aws_sdk_lex_models_v2.types.descriptive_bot_builder_specification.deserialize_json(
                data["descriptiveBotBuilder"]
            )
        )
    if "sampleUtteranceGeneration" in data:
        import aws_sdk_lex_models_v2.types.sample_utterance_generation_specification

        out["sample_utterance_generation"] = (
            aws_sdk_lex_models_v2.types.sample_utterance_generation_specification.deserialize_json(
                data["sampleUtteranceGeneration"]
            )
        )
    return out
