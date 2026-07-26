"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListAttachmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_list
    import capo_networkmanager.types.next_token


class ListAttachmentsResponse(TypedDict, closed=True):
    attachments: NotRequired["capo_networkmanager.types.attachment_list.AttachmentList"]
    """<p>Describes the list of attachments.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachmentsResponse) -> dict:
    out: dict = {}
    if "attachments" in value:
        import capo_networkmanager.types.attachment_list

        out["Attachments"] = capo_networkmanager.types.attachment_list.serialize_json(
            value["attachments"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttachmentsResponse:
    out: ListAttachmentsResponse = {}  # type: ignore[typeddict-item]
    if "Attachments" in data:
        import capo_networkmanager.types.attachment_list

        out["attachments"] = capo_networkmanager.types.attachment_list.deserialize_json(
            data["Attachments"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
