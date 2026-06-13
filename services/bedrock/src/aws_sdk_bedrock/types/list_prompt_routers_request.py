"""Generated from Smithy shape ``com.amazonaws.bedrock#ListPromptRoutersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.prompt_router_type


class ListPromptRoutersRequest(TypedDict):
    max_results: NotRequired["aws_sdk_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of prompt routers to return in one page of results.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    type: "aws_sdk_bedrock.types.prompt_router_type.PromptRouterType"
    """<p>The type of the prompt routers, such as whether it's default or custom.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPromptRoutersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPromptRoutersRequest:
    out: ListPromptRoutersRequest = {}  # type: ignore[typeddict-item]
    return out
