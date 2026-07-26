"""Generated from Smithy shape ``com.amazonaws.fis#ListExperimentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_summary_list
    import capo_fis.types.next_token


class ListExperimentsResponse(TypedDict, closed=True):
    experiments: NotRequired[
        "capo_fis.types.experiment_summary_list.ExperimentSummaryList"
    ]
    """<p>The experiments.</p>"""
    next_token: NotRequired["capo_fis.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExperimentsResponse) -> dict:
    out: dict = {}
    if "experiments" in value:
        import capo_fis.types.experiment_summary_list

        out["experiments"] = capo_fis.types.experiment_summary_list.serialize_json(
            value["experiments"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExperimentsResponse:
    out: ListExperimentsResponse = {}  # type: ignore[typeddict-item]
    if "experiments" in data:
        import capo_fis.types.experiment_summary_list

        out["experiments"] = capo_fis.types.experiment_summary_list.deserialize_json(
            data["experiments"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
