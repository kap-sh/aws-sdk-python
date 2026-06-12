"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ImageResponseCard``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.attachment_title
    import aws_sdk_lex_runtime_v2.types.attachment_url
    import aws_sdk_lex_runtime_v2.types.buttons_list


class ImageResponseCard(TypedDict):
    title: "aws_sdk_lex_runtime_v2.types.attachment_title.AttachmentTitle"
    """<p>The title to display on the response card. The format of the title is determined by the platform displaying the response card.</p>"""
    subtitle: NotRequired[
        "aws_sdk_lex_runtime_v2.types.attachment_title.AttachmentTitle"
    ]
    """<p>The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.</p>"""
    image_url: NotRequired["aws_sdk_lex_runtime_v2.types.attachment_url.AttachmentUrl"]
    """<p>The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.</p>"""
    buttons: NotRequired["aws_sdk_lex_runtime_v2.types.buttons_list.ButtonsList"]
    """<p>A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageResponseCard) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    if "subtitle" in value:
        out["subtitle"] = value["subtitle"]
    if "image_url" in value:
        out["imageUrl"] = value["image_url"]
    if "buttons" in value:
        import aws_sdk_lex_runtime_v2.types.buttons_list

        out["buttons"] = aws_sdk_lex_runtime_v2.types.buttons_list.serialize_json(
            value["buttons"]
        )
    return out


def deserialize_json(data: dict) -> ImageResponseCard:
    out: ImageResponseCard = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("ImageResponseCard.title required")
    if "subtitle" in data:
        out["subtitle"] = data["subtitle"]
    if "imageUrl" in data:
        out["image_url"] = data["imageUrl"]
    if "buttons" in data:
        import aws_sdk_lex_runtime_v2.types.buttons_list

        out["buttons"] = aws_sdk_lex_runtime_v2.types.buttons_list.deserialize_json(
            data["buttons"]
        )
    return out
