"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetSlotTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.slot_type_name
    import aws_sdk_lex_model_building_service.types.version


class GetSlotTypeRequest(TypedDict, closed=True):
    name: "aws_sdk_lex_model_building_service.types.slot_type_name.SlotTypeName"
    """<p>The name of the slot type. The name is case sensitive. </p>"""
    version: "aws_sdk_lex_model_building_service.types.version.Version"
    """<p>The version of the slot type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSlotTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSlotTypeRequest:
    out: GetSlotTypeRequest = {}  # type: ignore[typeddict-item]
    return out
