"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcases.types.text_attributes


class _FieldAttributes_text(TypedDict, closed=True):
    text: "capo_connectcases.types.text_attributes.TextAttributes"


FieldAttributes: TypeAlias = _FieldAttributes_text


# --- restJson1 ser/de ---
def serialize_json(value: FieldAttributes) -> dict:
    if "text" in value:
        import capo_connectcases.types.text_attributes

        return {
            "text": capo_connectcases.types.text_attributes.serialize_json(
                value["text"]
            )
        }
    else:
        raise SerializationError("FieldAttributes: no variant present")


def deserialize_json(data: dict) -> FieldAttributes:
    if "text" in data:
        import capo_connectcases.types.text_attributes

        return {
            "text": capo_connectcases.types.text_attributes.deserialize_json(
                data["text"]
            )
        }
    else:
        raise DeserializationError("FieldAttributes: no recognized variant key")
