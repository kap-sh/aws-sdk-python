"""Generated from Smithy shape ``com.amazonaws.omics#ListRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.batch_id
    import aws_sdk_omics.types.run_group_id
    import aws_sdk_omics.types.run_list_token
    import aws_sdk_omics.types.run_name
    import aws_sdk_omics.types.run_status


class ListRunsRequest(TypedDict, closed=True):
    name: NotRequired["aws_sdk_omics.types.run_name.RunName"]
    """<p>Filter the list by run name.</p>"""
    run_group_id: NotRequired["aws_sdk_omics.types.run_group_id.RunGroupId"]
    """<p>Filter the list by run group ID.</p>"""
    batch_id: NotRequired["aws_sdk_omics.types.batch_id.BatchId"]
    """<p>Filter by batch ID.</p>"""
    starting_token: NotRequired["aws_sdk_omics.types.run_list_token.RunListToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of runs to return in one page of results.</p>"""
    status: NotRequired["aws_sdk_omics.types.run_status.RunStatus"]
    """<p>The status of a run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRunsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRunsRequest:
    out: ListRunsRequest = {}  # type: ignore[typeddict-item]
    return out
