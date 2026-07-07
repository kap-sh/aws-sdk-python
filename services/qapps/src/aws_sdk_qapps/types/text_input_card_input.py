"""Generated from Smithy shape ``com.amazonaws.qapps#TextInputCardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.card_type
    import aws_sdk_qapps.types.default
    import aws_sdk_qapps.types.placeholder
    import aws_sdk_qapps.types.title
    import aws_sdk_qapps.types.uuid


class TextInputCardInput(TypedDict, closed=True):
    title: "aws_sdk_qapps.types.title.Title"
    """<p>The title or label of the text input card.</p>"""
    id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the text input card.</p>"""
    type: "aws_sdk_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    placeholder: NotRequired["aws_sdk_qapps.types.placeholder.Placeholder"]
    """<p>The placeholder text to display in the text input field.</p>"""
    default_value: NotRequired["aws_sdk_qapps.types.default.Default"]
    """<p>The default value to pre-populate in the text input field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextInputCardInput) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["id"] = value["id"]
    import aws_sdk_qapps.types.card_type

    out["type"] = aws_sdk_qapps.types.card_type.serialize_json(
        value.get("type", "text-input")
    )
    if "placeholder" in value:
        out["placeholder"] = value["placeholder"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> TextInputCardInput:
    out: TextInputCardInput = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("TextInputCardInput.title required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("TextInputCardInput.id required")
    if "type" in data:
        import aws_sdk_qapps.types.card_type

        out["type"] = aws_sdk_qapps.types.card_type.deserialize_json(data["type"])
    else:
        out["type"] = "text-input"
    if "placeholder" in data:
        out["placeholder"] = data["placeholder"]
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    return out
