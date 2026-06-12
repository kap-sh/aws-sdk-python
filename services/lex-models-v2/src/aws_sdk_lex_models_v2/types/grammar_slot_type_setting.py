"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GrammarSlotTypeSetting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.grammar_slot_type_source


class GrammarSlotTypeSetting(TypedDict):
    source: NotRequired[
        "aws_sdk_lex_models_v2.types.grammar_slot_type_source.GrammarSlotTypeSource"
    ]
    """<p>The source of the grammar used to create the slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrammarSlotTypeSetting) -> dict:
    out: dict = {}
    if "source" in value:
        import aws_sdk_lex_models_v2.types.grammar_slot_type_source

        out["source"] = (
            aws_sdk_lex_models_v2.types.grammar_slot_type_source.serialize_json(
                value["source"]
            )
        )
    return out


def deserialize_json(data: dict) -> GrammarSlotTypeSetting:
    out: GrammarSlotTypeSetting = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import aws_sdk_lex_models_v2.types.grammar_slot_type_source

        out["source"] = (
            aws_sdk_lex_models_v2.types.grammar_slot_type_source.deserialize_json(
                data["source"]
            )
        )
    return out
