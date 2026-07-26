"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#GenericAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.list_of_buttons
    import capo_lex_runtime_service.types.string_url_with_length
    import capo_lex_runtime_service.types.string_with_length


class GenericAttachment(TypedDict, closed=True):
    title: NotRequired[
        "capo_lex_runtime_service.types.string_with_length.StringWithLength"
    ]
    """<p>The title of the option.</p>"""
    sub_title: NotRequired[
        "capo_lex_runtime_service.types.string_with_length.StringWithLength"
    ]
    """<p>The subtitle shown below the title.</p>"""
    attachment_link_url: NotRequired[
        "capo_lex_runtime_service.types.string_url_with_length.StringUrlWithLength"
    ]
    """<p>The URL of an attachment to the response card.</p>"""
    image_url: NotRequired[
        "capo_lex_runtime_service.types.string_url_with_length.StringUrlWithLength"
    ]
    """<p>The URL of an image that is displayed to the user.</p>"""
    buttons: NotRequired["capo_lex_runtime_service.types.list_of_buttons.listOfButtons"]
    """<p>The list of options to show to the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenericAttachment) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "sub_title" in value:
        out["subTitle"] = value["sub_title"]
    if "attachment_link_url" in value:
        out["attachmentLinkUrl"] = value["attachment_link_url"]
    if "image_url" in value:
        out["imageUrl"] = value["image_url"]
    if "buttons" in value:
        import capo_lex_runtime_service.types.list_of_buttons

        out["buttons"] = capo_lex_runtime_service.types.list_of_buttons.serialize_json(
            value["buttons"]
        )
    return out


def deserialize_json(data: dict) -> GenericAttachment:
    out: GenericAttachment = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    if "subTitle" in data:
        out["sub_title"] = data["subTitle"]
    if "attachmentLinkUrl" in data:
        out["attachment_link_url"] = data["attachmentLinkUrl"]
    if "imageUrl" in data:
        out["image_url"] = data["imageUrl"]
    if "buttons" in data:
        import capo_lex_runtime_service.types.list_of_buttons

        out["buttons"] = (
            capo_lex_runtime_service.types.list_of_buttons.deserialize_json(
                data["buttons"]
            )
        )
    return out
