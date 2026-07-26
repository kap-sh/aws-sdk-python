"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListAttachedIndicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.index_attachment_list
    import capo_clouddirectory.types.next_token


class ListAttachedIndicesResponse(TypedDict, closed=True):
    index_attachments: NotRequired[
        "capo_clouddirectory.types.index_attachment_list.IndexAttachmentList"
    ]
    """<p>The indices attached to the specified object.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachedIndicesResponse) -> dict:
    out: dict = {}
    if "index_attachments" in value:
        import capo_clouddirectory.types.index_attachment_list

        out["IndexAttachments"] = (
            capo_clouddirectory.types.index_attachment_list.serialize_json(
                value["index_attachments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttachedIndicesResponse:
    out: ListAttachedIndicesResponse = {}  # type: ignore[typeddict-item]
    if "IndexAttachments" in data:
        import capo_clouddirectory.types.index_attachment_list

        out["index_attachments"] = (
            capo_clouddirectory.types.index_attachment_list.deserialize_json(
                data["IndexAttachments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
