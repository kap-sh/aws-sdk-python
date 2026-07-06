"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UserTurnIntentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.user_turn_slot_output_map


class UserTurnIntentOutput(TypedDict, closed=True):
    name: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The name of the intent.</p>"""
    slots: NotRequired[
        "aws_sdk_lex_models_v2.types.user_turn_slot_output_map.UserTurnSlotOutputMap"
    ]
    """<p>The slots associated with the intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserTurnIntentOutput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "slots" in value:
        import aws_sdk_lex_models_v2.types.user_turn_slot_output_map

        out["slots"] = (
            aws_sdk_lex_models_v2.types.user_turn_slot_output_map.serialize_json(
                value["slots"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserTurnIntentOutput:
    out: UserTurnIntentOutput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UserTurnIntentOutput.name required")
    if "slots" in data:
        import aws_sdk_lex_models_v2.types.user_turn_slot_output_map

        out["slots"] = (
            aws_sdk_lex_models_v2.types.user_turn_slot_output_map.deserialize_json(
                data["slots"]
            )
        )
    return out
