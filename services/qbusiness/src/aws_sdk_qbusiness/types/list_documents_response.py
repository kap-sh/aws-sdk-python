"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListDocumentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document_detail_list
    import aws_sdk_qbusiness.types.next_token


class ListDocumentsResponse(TypedDict, closed=True):
    document_detail_list: NotRequired[
        "aws_sdk_qbusiness.types.document_detail_list.DocumentDetailList"
    ]
    """<p>A list of document details.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of documents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDocumentsResponse) -> dict:
    out: dict = {}
    if "document_detail_list" in value:
        import aws_sdk_qbusiness.types.document_detail_list

        out["documentDetailList"] = (
            aws_sdk_qbusiness.types.document_detail_list.serialize_json(
                value["document_detail_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDocumentsResponse:
    out: ListDocumentsResponse = {}  # type: ignore[typeddict-item]
    if "documentDetailList" in data:
        import aws_sdk_qbusiness.types.document_detail_list

        out["document_detail_list"] = (
            aws_sdk_qbusiness.types.document_detail_list.deserialize_json(
                data["documentDetailList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
