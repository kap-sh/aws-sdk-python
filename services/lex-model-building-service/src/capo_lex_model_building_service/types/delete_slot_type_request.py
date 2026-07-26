"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#DeleteSlotTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.slot_type_name


class DeleteSlotTypeRequest(TypedDict, closed=True):
    name: "capo_lex_model_building_service.types.slot_type_name.SlotTypeName"
    """<p>The name of the slot type. The name is case sensitive. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSlotTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSlotTypeRequest:
    out: DeleteSlotTypeRequest = {}  # type: ignore[typeddict-item]
    return out
