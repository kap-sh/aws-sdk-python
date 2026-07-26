"""Generated from Smithy shape ``com.amazonaws.fis#ListExperimentResolvedTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_id
    import capo_fis.types.list_experiment_resolved_targets_max_results
    import capo_fis.types.next_token
    import capo_fis.types.target_name


class ListExperimentResolvedTargetsRequest(TypedDict, closed=True):
    experiment_id: "capo_fis.types.experiment_id.ExperimentId"
    """<p>The ID of the experiment.</p>"""
    max_results: NotRequired[
        "capo_fis.types.list_experiment_resolved_targets_max_results.ListExperimentResolvedTargetsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>"""
    next_token: NotRequired["capo_fis.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    target_name: NotRequired["capo_fis.types.target_name.TargetName"]
    """<p>The name of the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExperimentResolvedTargetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListExperimentResolvedTargetsRequest:
    out: ListExperimentResolvedTargetsRequest = {}  # type: ignore[typeddict-item]
    return out
