"""Generated from Smithy shape ``com.amazonaws.omics#ListRunsInBatchResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.list_token
    import aws_sdk_omics.types.run_batch_list


class ListRunsInBatchResponse(TypedDict, closed=True):
    runs: NotRequired["aws_sdk_omics.types.run_batch_list.RunBatchList"]
    """<p>A list of run entries in the batch. See <code>RunBatchListItem</code>.</p>"""
    next_token: NotRequired["aws_sdk_omics.types.list_token.ListToken"]
    """<p>A pagination token to retrieve the next page of results. Absent when the last run has been returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRunsInBatchResponse) -> dict:
    out: dict = {}
    if "runs" in value:
        import aws_sdk_omics.types.run_batch_list

        out["runs"] = aws_sdk_omics.types.run_batch_list.serialize_json(value["runs"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRunsInBatchResponse:
    out: ListRunsInBatchResponse = {}  # type: ignore[typeddict-item]
    if "runs" in data:
        import aws_sdk_omics.types.run_batch_list

        out["runs"] = aws_sdk_omics.types.run_batch_list.deserialize_json(data["runs"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
