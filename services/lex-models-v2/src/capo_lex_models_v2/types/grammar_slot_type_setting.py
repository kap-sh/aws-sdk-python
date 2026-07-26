"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GrammarSlotTypeSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.grammar_slot_type_source


class GrammarSlotTypeSetting(TypedDict, closed=True):
    source: NotRequired[
        "capo_lex_models_v2.types.grammar_slot_type_source.GrammarSlotTypeSource"
    ]
    """<p>The source of the grammar used to create the slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrammarSlotTypeSetting) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_lex_models_v2.types.grammar_slot_type_source

        out["source"] = (
            capo_lex_models_v2.types.grammar_slot_type_source.serialize_json(
                value["source"]
            )
        )
    return out


def deserialize_json(data: dict) -> GrammarSlotTypeSetting:
    out: GrammarSlotTypeSetting = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import capo_lex_models_v2.types.grammar_slot_type_source

        out["source"] = (
            capo_lex_models_v2.types.grammar_slot_type_source.deserialize_json(
                data["source"]
            )
        )
    return out
