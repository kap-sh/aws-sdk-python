"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#RuntimeHintDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.runtime_hint_values_list
    import aws_sdk_lex_runtime_v2.types.slot_hints_slot_map


class RuntimeHintDetails(TypedDict):
    runtime_hint_values: NotRequired[
        "aws_sdk_lex_runtime_v2.types.runtime_hint_values_list.RuntimeHintValuesList"
    ]
    """<p>One or more strings that Amazon Lex V2 should look for in the input to the bot. Each phrase is given preference when deciding on slot values.</p>"""
    sub_slot_hints: NotRequired[
        "aws_sdk_lex_runtime_v2.types.slot_hints_slot_map.SlotHintsSlotMap"
    ]
    """<p>A map of constituent sub slot names inside a composite slot in the intent and the phrases that should be added for each sub slot. Inside each composite slot hints, this structure provides a mechanism to add granular sub slot phrases. Only sub slot hints are supported for composite slots. The intent name, composite slot name and the constituent sub slot names must exist.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeHintDetails) -> dict:
    out: dict = {}
    if "runtime_hint_values" in value:
        import aws_sdk_lex_runtime_v2.types.runtime_hint_values_list

        out["runtimeHintValues"] = (
            aws_sdk_lex_runtime_v2.types.runtime_hint_values_list.serialize_json(
                value["runtime_hint_values"]
            )
        )
    if "sub_slot_hints" in value:
        import aws_sdk_lex_runtime_v2.types.slot_hints_slot_map

        out["subSlotHints"] = (
            aws_sdk_lex_runtime_v2.types.slot_hints_slot_map.serialize_json(
                value["sub_slot_hints"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuntimeHintDetails:
    out: RuntimeHintDetails = {}  # type: ignore[typeddict-item]
    if "runtimeHintValues" in data:
        import aws_sdk_lex_runtime_v2.types.runtime_hint_values_list

        out["runtime_hint_values"] = (
            aws_sdk_lex_runtime_v2.types.runtime_hint_values_list.deserialize_json(
                data["runtimeHintValues"]
            )
        )
    if "subSlotHints" in data:
        import aws_sdk_lex_runtime_v2.types.slot_hints_slot_map

        out["sub_slot_hints"] = (
            aws_sdk_lex_runtime_v2.types.slot_hints_slot_map.deserialize_json(
                data["subSlotHints"]
            )
        )
    return out
