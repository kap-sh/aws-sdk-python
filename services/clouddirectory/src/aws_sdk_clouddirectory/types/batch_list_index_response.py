"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchListIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.index_attachment_list
    import aws_sdk_clouddirectory.types.next_token


class BatchListIndexResponse(TypedDict, closed=True):
    index_attachments: NotRequired[
        "aws_sdk_clouddirectory.types.index_attachment_list.IndexAttachmentList"
    ]
    """<p>The objects and indexed values attached to the index.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchListIndexResponse) -> dict:
    out: dict = {}
    if "index_attachments" in value:
        import aws_sdk_clouddirectory.types.index_attachment_list

        out["IndexAttachments"] = (
            aws_sdk_clouddirectory.types.index_attachment_list.serialize_json(
                value["index_attachments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> BatchListIndexResponse:
    out: BatchListIndexResponse = {}  # type: ignore[typeddict-item]
    if "IndexAttachments" in data:
        import aws_sdk_clouddirectory.types.index_attachment_list

        out["index_attachments"] = (
            aws_sdk_clouddirectory.types.index_attachment_list.deserialize_json(
                data["IndexAttachments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
