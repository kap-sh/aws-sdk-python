"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#DeleteSlotTypeVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.numerical_version
    import capo_lex_model_building_service.types.slot_type_name


class DeleteSlotTypeVersionRequest(TypedDict, closed=True):
    name: "capo_lex_model_building_service.types.slot_type_name.SlotTypeName"
    """<p>The name of the slot type.</p>"""
    version: "capo_lex_model_building_service.types.numerical_version.NumericalVersion"
    """<p>The version of the slot type to delete. You cannot delete the <code>$LATEST</code> version of the slot type. To delete the <code>$LATEST</code> version, use the <a>DeleteSlotType</a> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSlotTypeVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSlotTypeVersionRequest:
    out: DeleteSlotTypeVersionRequest = {}  # type: ignore[typeddict-item]
    return out
