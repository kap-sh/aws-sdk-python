"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ElicitSubSlot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.elicit_sub_slot
    import aws_sdk_lex_runtime_v2.types.non_empty_string


class ElicitSubSlot(TypedDict, closed=True):
    name: "aws_sdk_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    """<p>The name of the slot that should be elicited from the user.</p>"""
    sub_slot_to_elicit: NotRequired[
        "aws_sdk_lex_runtime_v2.types.elicit_sub_slot.ElicitSubSlot"
    ]
    """<p>The field is not supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElicitSubSlot) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "sub_slot_to_elicit" in value:
        import aws_sdk_lex_runtime_v2.types.elicit_sub_slot

        out["subSlotToElicit"] = (
            aws_sdk_lex_runtime_v2.types.elicit_sub_slot.serialize_json(
                value["sub_slot_to_elicit"]
            )
        )
    return out


def deserialize_json(data: dict) -> ElicitSubSlot:
    out: ElicitSubSlot = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ElicitSubSlot.name required")
    if "subSlotToElicit" in data:
        import aws_sdk_lex_runtime_v2.types.elicit_sub_slot

        out["sub_slot_to_elicit"] = (
            aws_sdk_lex_runtime_v2.types.elicit_sub_slot.deserialize_json(
                data["subSlotToElicit"]
            )
        )
    return out
