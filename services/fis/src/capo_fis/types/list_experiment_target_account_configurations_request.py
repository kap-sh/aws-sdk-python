"""Generated from Smithy shape ``com.amazonaws.fis#ListExperimentTargetAccountConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_id
    import capo_fis.types.next_token


class ListExperimentTargetAccountConfigurationsRequest(TypedDict, closed=True):
    experiment_id: "capo_fis.types.experiment_id.ExperimentId"
    """<p>The ID of the experiment.</p>"""
    next_token: NotRequired["capo_fis.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExperimentTargetAccountConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListExperimentTargetAccountConfigurationsRequest:
    out: ListExperimentTargetAccountConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
