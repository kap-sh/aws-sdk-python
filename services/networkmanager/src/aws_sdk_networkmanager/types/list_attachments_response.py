"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListAttachmentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_list
    import aws_sdk_networkmanager.types.next_token


class ListAttachmentsResponse(TypedDict):
    attachments: NotRequired[
        "aws_sdk_networkmanager.types.attachment_list.AttachmentList"
    ]
    """<p>Describes the list of attachments.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachmentsResponse) -> dict:
    out: dict = {}
    if "attachments" in value:
        import aws_sdk_networkmanager.types.attachment_list

        out["Attachments"] = (
            aws_sdk_networkmanager.types.attachment_list.serialize_json(
                value["attachments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttachmentsResponse:
    out: ListAttachmentsResponse = {}  # type: ignore[typeddict-item]
    if "Attachments" in data:
        import aws_sdk_networkmanager.types.attachment_list

        out["attachments"] = (
            aws_sdk_networkmanager.types.attachment_list.deserialize_json(
                data["Attachments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
