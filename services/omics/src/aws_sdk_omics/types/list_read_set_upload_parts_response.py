"""Generated from Smithy shape ``com.amazonaws.omics#ListReadSetUploadPartsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.next_token
    import aws_sdk_omics.types.read_set_upload_part_list


class ListReadSetUploadPartsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_omics.types.next_token.NextToken"]
    """<p>Next token returned in the response of a previous ListReadSetUploadParts call. Used to get the next page of results.</p>"""
    parts: NotRequired[
        "aws_sdk_omics.types.read_set_upload_part_list.ReadSetUploadPartList"
    ]
    """<p>An array of upload parts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReadSetUploadPartsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "parts" in value:
        import aws_sdk_omics.types.read_set_upload_part_list

        out["parts"] = aws_sdk_omics.types.read_set_upload_part_list.serialize_json(
            value["parts"]
        )
    return out


def deserialize_json(data: dict) -> ListReadSetUploadPartsResponse:
    out: ListReadSetUploadPartsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "parts" in data:
        import aws_sdk_omics.types.read_set_upload_part_list

        out["parts"] = aws_sdk_omics.types.read_set_upload_part_list.deserialize_json(
            data["parts"]
        )
    return out
