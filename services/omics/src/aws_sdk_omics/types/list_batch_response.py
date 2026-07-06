"""Generated from Smithy shape ``com.amazonaws.omics#ListBatchResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.batch_list
    import aws_sdk_omics.types.list_token


class ListBatchResponse(TypedDict, closed=True):
    items: NotRequired["aws_sdk_omics.types.batch_list.BatchList"]
    """<p>A list of batch summary objects. See <code>BatchListItem</code>.</p>"""
    next_token: NotRequired["aws_sdk_omics.types.list_token.ListToken"]
    """<p>A pagination token to retrieve the next page of results. Absent when no further results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBatchResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_omics.types.batch_list

        out["items"] = aws_sdk_omics.types.batch_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBatchResponse:
    out: ListBatchResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_omics.types.batch_list

        out["items"] = aws_sdk_omics.types.batch_list.deserialize_json(data["items"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
