"""Generated from Smithy shape ``com.amazonaws.bedrock#ListPromptRoutersResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.prompt_router_summaries


class ListPromptRoutersResponse(TypedDict):
    prompt_router_summaries: NotRequired[
        "aws_sdk_bedrock.types.prompt_router_summaries.PromptRouterSummaries"
    ]
    """<p>A list of prompt router summaries.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPromptRoutersResponse) -> dict:
    out: dict = {}
    if "prompt_router_summaries" in value:
        import aws_sdk_bedrock.types.prompt_router_summaries

        out["promptRouterSummaries"] = (
            aws_sdk_bedrock.types.prompt_router_summaries.serialize_json(
                value["prompt_router_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPromptRoutersResponse:
    out: ListPromptRoutersResponse = {}  # type: ignore[typeddict-item]
    if "promptRouterSummaries" in data:
        import aws_sdk_bedrock.types.prompt_router_summaries

        out["prompt_router_summaries"] = (
            aws_sdk_bedrock.types.prompt_router_summaries.deserialize_json(
                data["promptRouterSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
