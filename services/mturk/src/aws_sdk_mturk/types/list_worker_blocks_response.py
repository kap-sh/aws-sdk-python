"""Generated from Smithy shape ``com.amazonaws.mturk#ListWorkerBlocksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mturk.types.integer
    import aws_sdk_mturk.types.pagination_token
    import aws_sdk_mturk.types.worker_block_list


class ListWorkerBlocksResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_mturk.types.pagination_token.PaginationToken"]
    num_results: NotRequired["aws_sdk_mturk.types.integer.Integer"]
    """<p> The number of assignments on the page in the filtered results list, equivalent to the number of assignments returned by this call.</p>"""
    worker_blocks: NotRequired["aws_sdk_mturk.types.worker_block_list.WorkerBlockList"]
    """<p> The list of WorkerBlocks, containing the collection of Worker IDs and reasons for blocking.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkerBlocksResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "num_results" in value:
        out["NumResults"] = value["num_results"]
    if "worker_blocks" in value:
        import aws_sdk_mturk.types.worker_block_list

        out["WorkerBlocks"] = (
            aws_sdk_mturk.types.worker_block_list.serialize_aws_json_1_1(
                value["worker_blocks"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkerBlocksResponse:
    out: ListWorkerBlocksResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "NumResults" in data:
        out["num_results"] = data["NumResults"]
    if "WorkerBlocks" in data:
        import aws_sdk_mturk.types.worker_block_list

        out["worker_blocks"] = (
            aws_sdk_mturk.types.worker_block_list.deserialize_aws_json_1_1(
                data["WorkerBlocks"]
            )
        )
    return out
