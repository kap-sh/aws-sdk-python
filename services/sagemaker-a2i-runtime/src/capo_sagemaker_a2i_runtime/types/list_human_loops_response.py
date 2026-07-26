"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#ListHumanLoopsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_a2i_runtime.types.human_loop_summaries
    import capo_sagemaker_a2i_runtime.types.next_token


class ListHumanLoopsResponse(TypedDict, closed=True):
    human_loop_summaries: NotRequired[
        "capo_sagemaker_a2i_runtime.types.human_loop_summaries.HumanLoopSummaries"
    ]
    """<p>An array of objects that contain information about the human loops.</p>"""
    next_token: NotRequired["capo_sagemaker_a2i_runtime.types.next_token.NextToken"]
    """<p>A token to display the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHumanLoopsResponse) -> dict:
    out: dict = {}
    if "human_loop_summaries" in value:
        import capo_sagemaker_a2i_runtime.types.human_loop_summaries

        out["HumanLoopSummaries"] = (
            capo_sagemaker_a2i_runtime.types.human_loop_summaries.serialize_json(
                value["human_loop_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListHumanLoopsResponse:
    out: ListHumanLoopsResponse = {}  # type: ignore[typeddict-item]
    if "HumanLoopSummaries" in data:
        import capo_sagemaker_a2i_runtime.types.human_loop_summaries

        out["human_loop_summaries"] = (
            capo_sagemaker_a2i_runtime.types.human_loop_summaries.deserialize_json(
                data["HumanLoopSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
