"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListAttachmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.attachment_list
    import capo_qbusiness.types.next_token


class ListAttachmentsResponse(TypedDict, closed=True):
    attachments: NotRequired["capo_qbusiness.types.attachment_list.AttachmentList"]
    """<p>An array of information on one or more attachments.</p>"""
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Q Business returns this token, which you can use in a later request to list the next set of attachments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachmentsResponse) -> dict:
    out: dict = {}
    if "attachments" in value:
        import capo_qbusiness.types.attachment_list

        out["attachments"] = capo_qbusiness.types.attachment_list.serialize_json(
            value["attachments"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttachmentsResponse:
    out: ListAttachmentsResponse = {}  # type: ignore[typeddict-item]
    if "attachments" in data:
        import capo_qbusiness.types.attachment_list

        out["attachments"] = capo_qbusiness.types.attachment_list.deserialize_json(
            data["attachments"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
