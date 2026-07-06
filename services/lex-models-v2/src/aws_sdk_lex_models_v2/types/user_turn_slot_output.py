"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UserTurnSlotOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.non_empty_string
    import aws_sdk_lex_models_v2.types.user_turn_slot_output_list
    import aws_sdk_lex_models_v2.types.user_turn_slot_output_map


class UserTurnSlotOutput(TypedDict, closed=True):
    value: NotRequired["aws_sdk_lex_models_v2.types.non_empty_string.NonEmptyString"]
    """<p>The value output by the slot recognition.</p>"""
    values: NotRequired[
        "aws_sdk_lex_models_v2.types.user_turn_slot_output_list.UserTurnSlotOutputList"
    ]
    """<p>Values that are output by the slot recognition.</p>"""
    sub_slots: NotRequired[
        "aws_sdk_lex_models_v2.types.user_turn_slot_output_map.UserTurnSlotOutputMap"
    ]
    """<p>A list of items mapping the name of the subslots to information about those subslots.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserTurnSlotOutput) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "values" in value:
        import aws_sdk_lex_models_v2.types.user_turn_slot_output_list

        out["values"] = (
            aws_sdk_lex_models_v2.types.user_turn_slot_output_list.serialize_json(
                value["values"]
            )
        )
    if "sub_slots" in value:
        import aws_sdk_lex_models_v2.types.user_turn_slot_output_map

        out["subSlots"] = (
            aws_sdk_lex_models_v2.types.user_turn_slot_output_map.serialize_json(
                value["sub_slots"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserTurnSlotOutput:
    out: UserTurnSlotOutput = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    if "values" in data:
        import aws_sdk_lex_models_v2.types.user_turn_slot_output_list

        out["values"] = (
            aws_sdk_lex_models_v2.types.user_turn_slot_output_list.deserialize_json(
                data["values"]
            )
        )
    if "subSlots" in data:
        import aws_sdk_lex_models_v2.types.user_turn_slot_output_map

        out["sub_slots"] = (
            aws_sdk_lex_models_v2.types.user_turn_slot_output_map.deserialize_json(
                data["subSlots"]
            )
        )
    return out
