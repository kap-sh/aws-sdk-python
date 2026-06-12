"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Message``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.image_response_card
    import aws_sdk_lex_runtime_v2.types.message_content_type
    import aws_sdk_lex_runtime_v2.types.text


class Message(TypedDict):
    content: NotRequired["aws_sdk_lex_runtime_v2.types.text.Text"]
    """<p>The text of the message.</p>"""
    content_type: "aws_sdk_lex_runtime_v2.types.message_content_type.MessageContentType"
    """<p>Indicates the type of response.</p>"""
    image_response_card: NotRequired[
        "aws_sdk_lex_runtime_v2.types.image_response_card.ImageResponseCard"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    if "content" in value:
        out["content"] = value["content"]
    import aws_sdk_lex_runtime_v2.types.message_content_type

    out["contentType"] = (
        aws_sdk_lex_runtime_v2.types.message_content_type.serialize_json(
            value["content_type"]
        )
    )
    if "image_response_card" in value:
        import aws_sdk_lex_runtime_v2.types.image_response_card

        out["imageResponseCard"] = (
            aws_sdk_lex_runtime_v2.types.image_response_card.serialize_json(
                value["image_response_card"]
            )
        )
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if "content" in data:
        out["content"] = data["content"]
    if "contentType" in data:
        import aws_sdk_lex_runtime_v2.types.message_content_type

        out["content_type"] = (
            aws_sdk_lex_runtime_v2.types.message_content_type.deserialize_json(
                data["contentType"]
            )
        )
    else:
        raise DeserializationError("Message.content_type required")
    if "imageResponseCard" in data:
        import aws_sdk_lex_runtime_v2.types.image_response_card

        out["image_response_card"] = (
            aws_sdk_lex_runtime_v2.types.image_response_card.deserialize_json(
                data["imageResponseCard"]
            )
        )
    return out
