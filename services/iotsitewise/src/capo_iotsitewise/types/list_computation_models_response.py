"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListComputationModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.computation_model_summaries
    import capo_iotsitewise.types.next_token


class ListComputationModelsResponse(TypedDict, closed=True):
    computation_model_summaries: (
        "capo_iotsitewise.types.computation_model_summaries.ComputationModelSummaries"
    )
    """<p>A list summarizing each computation model.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComputationModelsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.computation_model_summaries

    out["computationModelSummaries"] = (
        capo_iotsitewise.types.computation_model_summaries.serialize_json(
            value["computation_model_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComputationModelsResponse:
    out: ListComputationModelsResponse = {}  # type: ignore[typeddict-item]
    if "computationModelSummaries" in data:
        import capo_iotsitewise.types.computation_model_summaries

        out["computation_model_summaries"] = (
            capo_iotsitewise.types.computation_model_summaries.deserialize_json(
                data["computationModelSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListComputationModelsResponse.computation_model_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
