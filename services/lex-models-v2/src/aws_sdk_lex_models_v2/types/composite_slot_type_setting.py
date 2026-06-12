"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CompositeSlotTypeSetting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.sub_slot_type_list


class CompositeSlotTypeSetting(TypedDict):
    sub_slots: NotRequired[
        "aws_sdk_lex_models_v2.types.sub_slot_type_list.SubSlotTypeList"
    ]
    """<p>Subslots in the composite slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositeSlotTypeSetting) -> dict:
    out: dict = {}
    if "sub_slots" in value:
        import aws_sdk_lex_models_v2.types.sub_slot_type_list

        out["subSlots"] = aws_sdk_lex_models_v2.types.sub_slot_type_list.serialize_json(
            value["sub_slots"]
        )
    return out


def deserialize_json(data: dict) -> CompositeSlotTypeSetting:
    out: CompositeSlotTypeSetting = {}  # type: ignore[typeddict-item]
    if "subSlots" in data:
        import aws_sdk_lex_models_v2.types.sub_slot_type_list

        out["sub_slots"] = (
            aws_sdk_lex_models_v2.types.sub_slot_type_list.deserialize_json(
                data["subSlots"]
            )
        )
    return out
