"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentOverride``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.slot_value_override_map


class IntentOverride(TypedDict):
    name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The name of the intent. Only required when you're switching intents.</p>"""
    slots: NotRequired[
        "aws_sdk_lex_models_v2.types.slot_value_override_map.SlotValueOverrideMap"
    ]
    """<p>A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map aren't overridden.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentOverride) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "slots" in value:
        import aws_sdk_lex_models_v2.types.slot_value_override_map

        out["slots"] = (
            aws_sdk_lex_models_v2.types.slot_value_override_map.serialize_json(
                value["slots"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntentOverride:
    out: IntentOverride = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "slots" in data:
        import aws_sdk_lex_models_v2.types.slot_value_override_map

        out["slots"] = (
            aws_sdk_lex_models_v2.types.slot_value_override_map.deserialize_json(
                data["slots"]
            )
        )
    return out
