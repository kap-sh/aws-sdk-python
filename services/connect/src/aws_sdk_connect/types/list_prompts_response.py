"""Generated from Smithy shape ``com.amazonaws.connect#ListPromptsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.prompt_summary_list


class ListPromptsResponse(TypedDict):
    prompt_summary_list: NotRequired[
        "aws_sdk_connect.types.prompt_summary_list.PromptSummaryList"
    ]
    """<p>Information about the prompts.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPromptsResponse) -> dict:
    out: dict = {}
    if "prompt_summary_list" in value:
        import aws_sdk_connect.types.prompt_summary_list

        out["PromptSummaryList"] = (
            aws_sdk_connect.types.prompt_summary_list.serialize_json(
                value["prompt_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPromptsResponse:
    out: ListPromptsResponse = {}  # type: ignore[typeddict-item]
    if "PromptSummaryList" in data:
        import aws_sdk_connect.types.prompt_summary_list

        out["prompt_summary_list"] = (
            aws_sdk_connect.types.prompt_summary_list.deserialize_json(
                data["PromptSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
