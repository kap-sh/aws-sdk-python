"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListAttachmentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attachment_list
    import aws_sdk_qbusiness.types.next_token


class ListAttachmentsResponse(TypedDict):
    attachments: NotRequired["aws_sdk_qbusiness.types.attachment_list.AttachmentList"]
    """<p>An array of information on one or more attachments.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Q Business returns this token, which you can use in a later request to list the next set of attachments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachmentsResponse) -> dict:
    out: dict = {}
    if "attachments" in value:
        import aws_sdk_qbusiness.types.attachment_list

        out["attachments"] = aws_sdk_qbusiness.types.attachment_list.serialize_json(
            value["attachments"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttachmentsResponse:
    out: ListAttachmentsResponse = {}  # type: ignore[typeddict-item]
    if "attachments" in data:
        import aws_sdk_qbusiness.types.attachment_list

        out["attachments"] = aws_sdk_qbusiness.types.attachment_list.deserialize_json(
            data["attachments"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
