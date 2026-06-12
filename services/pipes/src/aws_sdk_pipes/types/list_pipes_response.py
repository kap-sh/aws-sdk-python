"""Generated from Smithy shape ``com.amazonaws.pipes#ListPipesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pipes.types.next_token
    import aws_sdk_pipes.types.pipe_list


class ListPipesResponse(TypedDict):
    pipes: NotRequired["aws_sdk_pipes.types.pipe_list.PipeList"]
    """<p>The pipes returned by the call.</p>"""
    next_token: NotRequired["aws_sdk_pipes.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipesResponse) -> dict:
    out: dict = {}
    if "pipes" in value:
        import aws_sdk_pipes.types.pipe_list

        out["Pipes"] = aws_sdk_pipes.types.pipe_list.serialize_json(value["pipes"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPipesResponse:
    out: ListPipesResponse = {}  # type: ignore[typeddict-item]
    if "Pipes" in data:
        import aws_sdk_pipes.types.pipe_list

        out["pipes"] = aws_sdk_pipes.types.pipe_list.deserialize_json(data["Pipes"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
