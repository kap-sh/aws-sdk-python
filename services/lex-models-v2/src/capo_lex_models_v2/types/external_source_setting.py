"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExternalSourceSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.grammar_slot_type_setting


class ExternalSourceSetting(TypedDict, closed=True):
    grammar_slot_type_setting: NotRequired[
        "capo_lex_models_v2.types.grammar_slot_type_setting.GrammarSlotTypeSetting"
    ]
    """<p>Settings required for a slot type based on a grammar that you provide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalSourceSetting) -> dict:
    out: dict = {}
    if "grammar_slot_type_setting" in value:
        import capo_lex_models_v2.types.grammar_slot_type_setting

        out["grammarSlotTypeSetting"] = (
            capo_lex_models_v2.types.grammar_slot_type_setting.serialize_json(
                value["grammar_slot_type_setting"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExternalSourceSetting:
    out: ExternalSourceSetting = {}  # type: ignore[typeddict-item]
    if "grammarSlotTypeSetting" in data:
        import capo_lex_models_v2.types.grammar_slot_type_setting

        out["grammar_slot_type_setting"] = (
            capo_lex_models_v2.types.grammar_slot_type_setting.deserialize_json(
                data["grammarSlotTypeSetting"]
            )
        )
    return out
