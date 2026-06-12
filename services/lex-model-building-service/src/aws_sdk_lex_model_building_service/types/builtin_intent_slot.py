"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#BuiltinIntentSlot``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.string


class BuiltinIntentSlot(TypedDict):
    name: NotRequired["aws_sdk_lex_model_building_service.types.string.String"]
    """<p>A list of the slots defined for the intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BuiltinIntentSlot) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> BuiltinIntentSlot:
    out: BuiltinIntentSlot = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
