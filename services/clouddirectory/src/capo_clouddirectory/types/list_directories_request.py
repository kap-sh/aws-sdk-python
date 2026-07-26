"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListDirectoriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.directory_state
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.number_results


class ListDirectoriesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired["capo_clouddirectory.types.number_results.NumberResults"]
    """<p>The maximum number of results to retrieve.</p>"""
    state: NotRequired["capo_clouddirectory.types.directory_state.DirectoryState"]
    """<p>The state of the directories in the list. Can be either Enabled, Disabled, or Deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDirectoriesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "state" in value:
        import capo_clouddirectory.types.directory_state

        out["state"] = capo_clouddirectory.types.directory_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> ListDirectoriesRequest:
    out: ListDirectoriesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "state" in data:
        import capo_clouddirectory.types.directory_state

        out["state"] = capo_clouddirectory.types.directory_state.deserialize_json(
            data["state"]
        )
    return out
