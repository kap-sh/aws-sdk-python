"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceBotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.image_response_card
    import aws_sdk_lex_models_v2.types.string
    import aws_sdk_lex_models_v2.types.utterance_content_type


class UtteranceBotResponse(TypedDict, closed=True):
    content: NotRequired["aws_sdk_lex_models_v2.types.string.String"]
    """<p>The text of the response to the utterance from the bot.</p>"""
    content_type: NotRequired[
        "aws_sdk_lex_models_v2.types.utterance_content_type.UtteranceContentType"
    ]
    r"""<p>The type of the response. The following values are possible:</p> <ul> <li> <p> <code>PlainText</code> – A plain text string.</p> </li> <li> <p> <code>CustomPayload</code> – A response string that you can customize to include data or metadata for your application.</p> </li> <li> <p> <code>SSML</code> – A string that includes Speech Synthesis Markup Language to customize the audio response.</p> </li> <li> <p> <code>ImageResponseCard</code> – An image with buttons that the customer can select. See <a href=\"https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_ImageResponseCard.html\">ImageResponseCard</a> for more information.</p> </li> </ul>"""
    image_response_card: NotRequired[
        "aws_sdk_lex_models_v2.types.image_response_card.ImageResponseCard"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceBotResponse) -> dict:
    out: dict = {}
    if "content" in value:
        out["content"] = value["content"]
    if "content_type" in value:
        import aws_sdk_lex_models_v2.types.utterance_content_type

        out["contentType"] = (
            aws_sdk_lex_models_v2.types.utterance_content_type.serialize_json(
                value["content_type"]
            )
        )
    if "image_response_card" in value:
        import aws_sdk_lex_models_v2.types.image_response_card

        out["imageResponseCard"] = (
            aws_sdk_lex_models_v2.types.image_response_card.serialize_json(
                value["image_response_card"]
            )
        )
    return out


def deserialize_json(data: dict) -> UtteranceBotResponse:
    out: UtteranceBotResponse = {}  # type: ignore[typeddict-item]
    if "content" in data:
        out["content"] = data["content"]
    if "contentType" in data:
        import aws_sdk_lex_models_v2.types.utterance_content_type

        out["content_type"] = (
            aws_sdk_lex_models_v2.types.utterance_content_type.deserialize_json(
                data["contentType"]
            )
        )
    if "imageResponseCard" in data:
        import aws_sdk_lex_models_v2.types.image_response_card

        out["image_response_card"] = (
            aws_sdk_lex_models_v2.types.image_response_card.deserialize_json(
                data["imageResponseCard"]
            )
        )
    return out
