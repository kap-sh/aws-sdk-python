"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListComputationModelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.computation_model_type
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token


class ListComputationModelsRequest(TypedDict, closed=True):
    computation_model_type: NotRequired[
        "capo_iotsitewise.types.computation_model_type.ComputationModelType"
    ]
    """<p>The type of computation model. If a <code>computationModelType</code> is not provided, all types of computation models are returned.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComputationModelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListComputationModelsRequest:
    out: ListComputationModelsRequest = {}  # type: ignore[typeddict-item]
    return out
