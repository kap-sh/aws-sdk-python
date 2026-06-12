"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExternalSourceSetting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.grammar_slot_type_setting


class ExternalSourceSetting(TypedDict):
    grammar_slot_type_setting: NotRequired[
        "aws_sdk_lex_models_v2.types.grammar_slot_type_setting.GrammarSlotTypeSetting"
    ]
    """<p>Settings required for a slot type based on a grammar that you provide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalSourceSetting) -> dict:
    out: dict = {}
    if "grammar_slot_type_setting" in value:
        import aws_sdk_lex_models_v2.types.grammar_slot_type_setting

        out["grammarSlotTypeSetting"] = (
            aws_sdk_lex_models_v2.types.grammar_slot_type_setting.serialize_json(
                value["grammar_slot_type_setting"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExternalSourceSetting:
    out: ExternalSourceSetting = {}  # type: ignore[typeddict-item]
    if "grammarSlotTypeSetting" in data:
        import aws_sdk_lex_models_v2.types.grammar_slot_type_setting

        out["grammar_slot_type_setting"] = (
            aws_sdk_lex_models_v2.types.grammar_slot_type_setting.deserialize_json(
                data["grammarSlotTypeSetting"]
            )
        )
    return out
