"""Generated from Smithy shape ``com.amazonaws.omics#ListRunGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.run_group_list_token
    import capo_omics.types.run_group_name


class ListRunGroupsRequest(TypedDict, closed=True):
    name: NotRequired["capo_omics.types.run_group_name.RunGroupName"]
    """<p>The run groups' name.</p>"""
    starting_token: NotRequired[
        "capo_omics.types.run_group_list_token.RunGroupListToken"
    ]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of run groups to return in one page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRunGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRunGroupsRequest:
    out: ListRunGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
