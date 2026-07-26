"""Generated from Smithy shape ``com.amazonaws.connect#ListPromptsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token
    import capo_connect.types.prompt_summary_list


class ListPromptsResponse(TypedDict, closed=True):
    prompt_summary_list: NotRequired[
        "capo_connect.types.prompt_summary_list.PromptSummaryList"
    ]
    """<p>Information about the prompts.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPromptsResponse) -> dict:
    out: dict = {}
    if "prompt_summary_list" in value:
        import capo_connect.types.prompt_summary_list

        out["PromptSummaryList"] = (
            capo_connect.types.prompt_summary_list.serialize_json(
                value["prompt_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPromptsResponse:
    out: ListPromptsResponse = {}  # type: ignore[typeddict-item]
    if "PromptSummaryList" in data:
        import capo_connect.types.prompt_summary_list

        out["prompt_summary_list"] = (
            capo_connect.types.prompt_summary_list.deserialize_json(
                data["PromptSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
