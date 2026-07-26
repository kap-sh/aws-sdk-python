"""Generated from Smithy shape ``com.amazonaws.fis#ListTargetAccountConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_id
    import capo_fis.types.list_target_account_configurations_max_results
    import capo_fis.types.next_token


class ListTargetAccountConfigurationsRequest(TypedDict, closed=True):
    experiment_template_id: "capo_fis.types.experiment_template_id.ExperimentTemplateId"
    """<p>The ID of the experiment template.</p>"""
    max_results: NotRequired[
        "capo_fis.types.list_target_account_configurations_max_results.ListTargetAccountConfigurationsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>"""
    next_token: NotRequired["capo_fis.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetAccountConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTargetAccountConfigurationsRequest:
    out: ListTargetAccountConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
