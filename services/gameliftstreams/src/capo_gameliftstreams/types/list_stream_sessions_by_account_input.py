"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ListStreamSessionsByAccountInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.export_files_status
    import capo_gameliftstreams.types.max_results
    import capo_gameliftstreams.types.next_token
    import capo_gameliftstreams.types.stream_session_status


class ListStreamSessionsByAccountInput(TypedDict, closed=True):
    status: NotRequired[
        "capo_gameliftstreams.types.stream_session_status.StreamSessionStatus"
    ]
    """<p>Filter by the stream session status. You can specify one status in each request to retrieve only sessions that are currently in that status.</p>"""
    export_files_status: NotRequired[
        "capo_gameliftstreams.types.export_files_status.ExportFilesStatus"
    ]
    """<p>Filter by the exported files status. You can specify one status in each request to retrieve only sessions that currently have that exported files status.</p>"""
    next_token: NotRequired["capo_gameliftstreams.types.next_token.NextToken"]
    """<p>The token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set. </p>"""
    max_results: NotRequired["capo_gameliftstreams.types.max_results.MaxResults"]
    """<p>The number of results to return. Use this parameter with <code>NextToken</code> to return results in sequential pages. Default value is <code>25</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamSessionsByAccountInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListStreamSessionsByAccountInput:
    out: ListStreamSessionsByAccountInput = {}  # type: ignore[typeddict-item]
    return out
