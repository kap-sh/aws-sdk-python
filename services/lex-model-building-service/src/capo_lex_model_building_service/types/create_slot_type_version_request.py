"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#CreateSlotTypeVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.slot_type_name
    import capo_lex_model_building_service.types.string


class CreateSlotTypeVersionRequest(TypedDict, closed=True):
    name: "capo_lex_model_building_service.types.slot_type_name.SlotTypeName"
    """<p>The name of the slot type that you want to create a new version for. The name is case sensitive. </p>"""
    checksum: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>Checksum for the <code>$LATEST</code> version of the slot type that you want to publish. If you specify a checksum and the <code>$LATEST</code> version of the slot type has a different checksum, Amazon Lex returns a <code>PreconditionFailedException</code> exception and doesn't publish the new version. If you don't specify a checksum, Amazon Lex publishes the <code>$LATEST</code> version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSlotTypeVersionRequest) -> dict:
    out: dict = {}
    if "checksum" in value:
        out["checksum"] = value["checksum"]
    return out


def deserialize_json(data: dict) -> CreateSlotTypeVersionRequest:
    out: CreateSlotTypeVersionRequest = {}  # type: ignore[typeddict-item]
    if "checksum" in data:
        out["checksum"] = data["checksum"]
    return out
