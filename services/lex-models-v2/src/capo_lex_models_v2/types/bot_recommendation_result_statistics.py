"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotRecommendationResultStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.intent_statistics
    import capo_lex_models_v2.types.slot_type_statistics


class BotRecommendationResultStatistics(TypedDict, closed=True):
    intents: NotRequired["capo_lex_models_v2.types.intent_statistics.IntentStatistics"]
    """<p>Statistical information about about the intents associated with the bot recommendation results.</p>"""
    slot_types: NotRequired[
        "capo_lex_models_v2.types.slot_type_statistics.SlotTypeStatistics"
    ]
    """<p>Statistical information about the slot types associated with the bot recommendation results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotRecommendationResultStatistics) -> dict:
    out: dict = {}
    if "intents" in value:
        import capo_lex_models_v2.types.intent_statistics

        out["intents"] = capo_lex_models_v2.types.intent_statistics.serialize_json(
            value["intents"]
        )
    if "slot_types" in value:
        import capo_lex_models_v2.types.slot_type_statistics

        out["slotTypes"] = capo_lex_models_v2.types.slot_type_statistics.serialize_json(
            value["slot_types"]
        )
    return out


def deserialize_json(data: dict) -> BotRecommendationResultStatistics:
    out: BotRecommendationResultStatistics = {}  # type: ignore[typeddict-item]
    if "intents" in data:
        import capo_lex_models_v2.types.intent_statistics

        out["intents"] = capo_lex_models_v2.types.intent_statistics.deserialize_json(
            data["intents"]
        )
    if "slotTypes" in data:
        import capo_lex_models_v2.types.slot_type_statistics

        out["slot_types"] = (
            capo_lex_models_v2.types.slot_type_statistics.deserialize_json(
                data["slotTypes"]
            )
        )
    return out
