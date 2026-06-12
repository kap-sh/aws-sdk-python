"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Message``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.content_string
    import aws_sdk_lex_model_building_service.types.content_type
    import aws_sdk_lex_model_building_service.types.group_number


class Message(TypedDict):
    content_type: "aws_sdk_lex_model_building_service.types.content_type.ContentType"
    """<p>The content type of the message string.</p>"""
    content: "aws_sdk_lex_model_building_service.types.content_string.ContentString"
    """<p>The text of the message.</p>"""
    group_number: NotRequired[
        "aws_sdk_lex_model_building_service.types.group_number.GroupNumber"
    ]
    """<p>Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    import aws_sdk_lex_model_building_service.types.content_type

    out["contentType"] = (
        aws_sdk_lex_model_building_service.types.content_type.serialize_json(
            value["content_type"]
        )
    )
    out["content"] = value["content"]
    if "group_number" in value:
        out["groupNumber"] = value["group_number"]
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if "contentType" in data:
        import aws_sdk_lex_model_building_service.types.content_type

        out["content_type"] = (
            aws_sdk_lex_model_building_service.types.content_type.deserialize_json(
                data["contentType"]
            )
        )
    else:
        raise DeserializationError("Message.content_type required")
    if "content" in data:
        out["content"] = data["content"]
    else:
        raise DeserializationError("Message.content required")
    if "groupNumber" in data:
        out["group_number"] = data["groupNumber"]
    return out
