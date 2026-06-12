"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SubSlotTypeComposition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.built_in_or_custom_slot_type_id
    import aws_sdk_lex_models_v2.types.name


class SubSlotTypeComposition(TypedDict):
    name: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>Name of a constituent sub slot inside a composite slot.</p>"""
    slot_type_id: "aws_sdk_lex_models_v2.types.built_in_or_custom_slot_type_id.BuiltInOrCustomSlotTypeId"
    """<p>The unique identifier assigned to a slot type. This refers to either a built-in slot type or the unique slotTypeId of a custom slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubSlotTypeComposition) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["slotTypeId"] = value["slot_type_id"]
    return out


def deserialize_json(data: dict) -> SubSlotTypeComposition:
    out: SubSlotTypeComposition = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SubSlotTypeComposition.name required")
    if "slotTypeId" in data:
        out["slot_type_id"] = data["slotTypeId"]
    else:
        raise DeserializationError("SubSlotTypeComposition.slot_type_id required")
    return out
