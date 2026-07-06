"""Generated from Smithy shape ``com.amazonaws.omics#ListMultipartReadSetUploadsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.multipart_read_set_upload_list
    import aws_sdk_omics.types.next_token


class ListMultipartReadSetUploadsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_omics.types.next_token.NextToken"]
    """<p>Next token returned in the response of a previous ListMultipartReadSetUploads call. Used to get the next page of results.</p>"""
    uploads: NotRequired[
        "aws_sdk_omics.types.multipart_read_set_upload_list.MultipartReadSetUploadList"
    ]
    """<p>An array of multipart uploads.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMultipartReadSetUploadsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "uploads" in value:
        import aws_sdk_omics.types.multipart_read_set_upload_list

        out["uploads"] = (
            aws_sdk_omics.types.multipart_read_set_upload_list.serialize_json(
                value["uploads"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListMultipartReadSetUploadsResponse:
    out: ListMultipartReadSetUploadsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "uploads" in data:
        import aws_sdk_omics.types.multipart_read_set_upload_list

        out["uploads"] = (
            aws_sdk_omics.types.multipart_read_set_upload_list.deserialize_json(
                data["uploads"]
            )
        )
    return out
