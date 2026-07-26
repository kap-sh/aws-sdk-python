"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BuiltInSlotTypeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.slot_type_signature


class BuiltInSlotTypeSummary(TypedDict, closed=True):
    slot_type_signature: NotRequired[
        "capo_lex_models_v2.types.slot_type_signature.SlotTypeSignature"
    ]
    """<p>The signature of the built-in slot type. Use this to specify the parent slot type of a derived slot type.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The description of the built-in slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BuiltInSlotTypeSummary) -> dict:
    out: dict = {}
    if "slot_type_signature" in value:
        out["slotTypeSignature"] = value["slot_type_signature"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> BuiltInSlotTypeSummary:
    out: BuiltInSlotTypeSummary = {}  # type: ignore[typeddict-item]
    if "slotTypeSignature" in data:
        out["slot_type_signature"] = data["slotTypeSignature"]
    if "description" in data:
        out["description"] = data["description"]
    return out
