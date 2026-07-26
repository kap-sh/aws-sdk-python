"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#ResponseCard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.content_type
    import capo_lex_runtime_service.types.generic_attachment_list
    import capo_lex_runtime_service.types.string


class ResponseCard(TypedDict, closed=True):
    version: NotRequired["capo_lex_runtime_service.types.string.String"]
    """<p>The version of the response card format.</p>"""
    content_type: NotRequired["capo_lex_runtime_service.types.content_type.ContentType"]
    """<p>The content type of the response.</p>"""
    generic_attachments: NotRequired[
        "capo_lex_runtime_service.types.generic_attachment_list.genericAttachmentList"
    ]
    """<p>An array of attachment objects representing options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseCard) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    if "content_type" in value:
        import capo_lex_runtime_service.types.content_type

        out["contentType"] = capo_lex_runtime_service.types.content_type.serialize_json(
            value["content_type"]
        )
    if "generic_attachments" in value:
        import capo_lex_runtime_service.types.generic_attachment_list

        out["genericAttachments"] = (
            capo_lex_runtime_service.types.generic_attachment_list.serialize_json(
                value["generic_attachments"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResponseCard:
    out: ResponseCard = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    if "contentType" in data:
        import capo_lex_runtime_service.types.content_type

        out["content_type"] = (
            capo_lex_runtime_service.types.content_type.deserialize_json(
                data["contentType"]
            )
        )
    if "genericAttachments" in data:
        import capo_lex_runtime_service.types.generic_attachment_list

        out["generic_attachments"] = (
            capo_lex_runtime_service.types.generic_attachment_list.deserialize_json(
                data["genericAttachments"]
            )
        )
    return out
