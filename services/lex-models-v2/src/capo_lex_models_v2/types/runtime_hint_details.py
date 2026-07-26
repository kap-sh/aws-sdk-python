"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#RuntimeHintDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.runtime_hint_values_list
    import capo_lex_models_v2.types.slot_hints_slot_map


class RuntimeHintDetails(TypedDict, closed=True):
    runtime_hint_values: NotRequired[
        "capo_lex_models_v2.types.runtime_hint_values_list.RuntimeHintValuesList"
    ]
    """<p>One or more strings that Amazon Lex should look for in the input to the bot. Each phrase is given preference when deciding on slot values.</p>"""
    sub_slot_hints: NotRequired[
        "capo_lex_models_v2.types.slot_hints_slot_map.SlotHintsSlotMap"
    ]
    """<p>A map of constituent sub slot names inside a composite slot in the intent and the phrases that should be added for each sub slot. Inside each composite slot hints, this structure provides a mechanism to add granular sub slot phrases. Only sub slot hints are supported for composite slots. The intent name, composite slot name and the constituent sub slot names must exist.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeHintDetails) -> dict:
    out: dict = {}
    if "runtime_hint_values" in value:
        import capo_lex_models_v2.types.runtime_hint_values_list

        out["runtimeHintValues"] = (
            capo_lex_models_v2.types.runtime_hint_values_list.serialize_json(
                value["runtime_hint_values"]
            )
        )
    if "sub_slot_hints" in value:
        import capo_lex_models_v2.types.slot_hints_slot_map

        out["subSlotHints"] = (
            capo_lex_models_v2.types.slot_hints_slot_map.serialize_json(
                value["sub_slot_hints"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuntimeHintDetails:
    out: RuntimeHintDetails = {}  # type: ignore[typeddict-item]
    if "runtimeHintValues" in data:
        import capo_lex_models_v2.types.runtime_hint_values_list

        out["runtime_hint_values"] = (
            capo_lex_models_v2.types.runtime_hint_values_list.deserialize_json(
                data["runtimeHintValues"]
            )
        )
    if "subSlotHints" in data:
        import capo_lex_models_v2.types.slot_hints_slot_map

        out["sub_slot_hints"] = (
            capo_lex_models_v2.types.slot_hints_slot_map.deserialize_json(
                data["subSlotHints"]
            )
        )
    return out
