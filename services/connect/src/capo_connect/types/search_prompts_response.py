"""Generated from Smithy shape ``com.amazonaws.connect#SearchPromptsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.next_token2500
    import capo_connect.types.prompt_list


class SearchPromptsResponse(TypedDict, closed=True):
    prompts: NotRequired["capo_connect.types.prompt_list.PromptList"]
    """<p>Information about the prompts.</p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of quick connects which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchPromptsResponse) -> dict:
    out: dict = {}
    if "prompts" in value:
        import capo_connect.types.prompt_list

        out["Prompts"] = capo_connect.types.prompt_list.serialize_json(value["prompts"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchPromptsResponse:
    out: SearchPromptsResponse = {}  # type: ignore[typeddict-item]
    if "Prompts" in data:
        import capo_connect.types.prompt_list

        out["prompts"] = capo_connect.types.prompt_list.deserialize_json(
            data["Prompts"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
