"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CompositeSlotTypeSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.sub_slot_type_list


class CompositeSlotTypeSetting(TypedDict, closed=True):
    sub_slots: NotRequired[
        "capo_lex_models_v2.types.sub_slot_type_list.SubSlotTypeList"
    ]
    """<p>Subslots in the composite slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositeSlotTypeSetting) -> dict:
    out: dict = {}
    if "sub_slots" in value:
        import capo_lex_models_v2.types.sub_slot_type_list

        out["subSlots"] = capo_lex_models_v2.types.sub_slot_type_list.serialize_json(
            value["sub_slots"]
        )
    return out


def deserialize_json(data: dict) -> CompositeSlotTypeSetting:
    out: CompositeSlotTypeSetting = {}  # type: ignore[typeddict-item]
    if "subSlots" in data:
        import capo_lex_models_v2.types.sub_slot_type_list

        out["sub_slots"] = capo_lex_models_v2.types.sub_slot_type_list.deserialize_json(
            data["subSlots"]
        )
    return out
