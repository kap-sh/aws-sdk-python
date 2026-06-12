"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#Message``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.custom_payload
    import aws_sdk_lex_models_v2.types.image_response_card
    import aws_sdk_lex_models_v2.types.plain_text_message
    import aws_sdk_lex_models_v2.types.ssml_message


class Message(TypedDict):
    plain_text_message: NotRequired[
        "aws_sdk_lex_models_v2.types.plain_text_message.PlainTextMessage"
    ]
    """<p>A message in plain text format.</p>"""
    custom_payload: NotRequired[
        "aws_sdk_lex_models_v2.types.custom_payload.CustomPayload"
    ]
    """<p>A message in a custom format defined by the client application.</p>"""
    ssml_message: NotRequired["aws_sdk_lex_models_v2.types.ssml_message.SSMLMessage"]
    """<p>A message in Speech Synthesis Markup Language (SSML).</p>"""
    image_response_card: NotRequired[
        "aws_sdk_lex_models_v2.types.image_response_card.ImageResponseCard"
    ]
    """<p>A message that defines a response card that the client application can show to the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    if "plain_text_message" in value:
        import aws_sdk_lex_models_v2.types.plain_text_message

        out["plainTextMessage"] = (
            aws_sdk_lex_models_v2.types.plain_text_message.serialize_json(
                value["plain_text_message"]
            )
        )
    if "custom_payload" in value:
        import aws_sdk_lex_models_v2.types.custom_payload

        out["customPayload"] = (
            aws_sdk_lex_models_v2.types.custom_payload.serialize_json(
                value["custom_payload"]
            )
        )
    if "ssml_message" in value:
        import aws_sdk_lex_models_v2.types.ssml_message

        out["ssmlMessage"] = aws_sdk_lex_models_v2.types.ssml_message.serialize_json(
            value["ssml_message"]
        )
    if "image_response_card" in value:
        import aws_sdk_lex_models_v2.types.image_response_card

        out["imageResponseCard"] = (
            aws_sdk_lex_models_v2.types.image_response_card.serialize_json(
                value["image_response_card"]
            )
        )
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if "plainTextMessage" in data:
        import aws_sdk_lex_models_v2.types.plain_text_message

        out["plain_text_message"] = (
            aws_sdk_lex_models_v2.types.plain_text_message.deserialize_json(
                data["plainTextMessage"]
            )
        )
    if "customPayload" in data:
        import aws_sdk_lex_models_v2.types.custom_payload

        out["custom_payload"] = (
            aws_sdk_lex_models_v2.types.custom_payload.deserialize_json(
                data["customPayload"]
            )
        )
    if "ssmlMessage" in data:
        import aws_sdk_lex_models_v2.types.ssml_message

        out["ssml_message"] = aws_sdk_lex_models_v2.types.ssml_message.deserialize_json(
            data["ssmlMessage"]
        )
    if "imageResponseCard" in data:
        import aws_sdk_lex_models_v2.types.image_response_card

        out["image_response_card"] = (
            aws_sdk_lex_models_v2.types.image_response_card.deserialize_json(
                data["imageResponseCard"]
            )
        )
    return out
