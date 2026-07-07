"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#RuntimeSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.nlu_improvement_specification
    import aws_sdk_lex_models_v2.types.slot_resolution_improvement_specification


class RuntimeSettings(TypedDict, closed=True):
    slot_resolution_improvement: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_resolution_improvement_specification.SlotResolutionImprovementSpecification"
    ]
    """<p>An object containing specifications for the assisted slot resolution feature.</p>"""
    nlu_improvement: NotRequired[
        "aws_sdk_lex_models_v2.types.nlu_improvement_specification.NluImprovementSpecification"
    ]
    """<p>An object containing specifications for the Assisted NLU feature within the bot's runtime settings. These settings determine how the bot processes and interprets user utterances during conversations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeSettings) -> dict:
    out: dict = {}
    if "slot_resolution_improvement" in value:
        import aws_sdk_lex_models_v2.types.slot_resolution_improvement_specification

        out["slotResolutionImprovement"] = (
            aws_sdk_lex_models_v2.types.slot_resolution_improvement_specification.serialize_json(
                value["slot_resolution_improvement"]
            )
        )
    if "nlu_improvement" in value:
        import aws_sdk_lex_models_v2.types.nlu_improvement_specification

        out["nluImprovement"] = (
            aws_sdk_lex_models_v2.types.nlu_improvement_specification.serialize_json(
                value["nlu_improvement"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuntimeSettings:
    out: RuntimeSettings = {}  # type: ignore[typeddict-item]
    if "slotResolutionImprovement" in data:
        import aws_sdk_lex_models_v2.types.slot_resolution_improvement_specification

        out["slot_resolution_improvement"] = (
            aws_sdk_lex_models_v2.types.slot_resolution_improvement_specification.deserialize_json(
                data["slotResolutionImprovement"]
            )
        )
    if "nluImprovement" in data:
        import aws_sdk_lex_models_v2.types.nlu_improvement_specification

        out["nlu_improvement"] = (
            aws_sdk_lex_models_v2.types.nlu_improvement_specification.deserialize_json(
                data["nluImprovement"]
            )
        )
    return out
