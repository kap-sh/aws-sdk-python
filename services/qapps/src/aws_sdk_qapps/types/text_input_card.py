"""Generated from Smithy shape ``com.amazonaws.qapps#TextInputCard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.card_type
    import aws_sdk_qapps.types.default
    import aws_sdk_qapps.types.dependency_list
    import aws_sdk_qapps.types.placeholder
    import aws_sdk_qapps.types.title
    import aws_sdk_qapps.types.uuid


class TextInputCard(TypedDict, closed=True):
    id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the text input card.</p>"""
    title: "aws_sdk_qapps.types.title.Title"
    """<p>The title or label of the text input card.</p>"""
    dependencies: "aws_sdk_qapps.types.dependency_list.DependencyList"
    """<p>Any dependencies or requirements for the text input card.</p>"""
    type: "aws_sdk_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    placeholder: NotRequired["aws_sdk_qapps.types.placeholder.Placeholder"]
    """<p>The placeholder text to display in the text input field.</p>"""
    default_value: NotRequired["aws_sdk_qapps.types.default.Default"]
    """<p>The default value to pre-populate in the text input field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextInputCard) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["title"] = value["title"]
    import aws_sdk_qapps.types.dependency_list

    out["dependencies"] = aws_sdk_qapps.types.dependency_list.serialize_json(
        value["dependencies"]
    )
    import aws_sdk_qapps.types.card_type

    out["type"] = aws_sdk_qapps.types.card_type.serialize_json(value["type"])
    if "placeholder" in value:
        out["placeholder"] = value["placeholder"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> TextInputCard:
    out: TextInputCard = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("TextInputCard.id required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("TextInputCard.title required")
    if "dependencies" in data:
        import aws_sdk_qapps.types.dependency_list

        out["dependencies"] = aws_sdk_qapps.types.dependency_list.deserialize_json(
            data["dependencies"]
        )
    else:
        raise DeserializationError("TextInputCard.dependencies required")
    if "type" in data:
        import aws_sdk_qapps.types.card_type

        out["type"] = aws_sdk_qapps.types.card_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("TextInputCard.type required")
    if "placeholder" in data:
        out["placeholder"] = data["placeholder"]
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    return out
