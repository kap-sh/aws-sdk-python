"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListContainerRecipesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.container_recipe_summary_list
    import capo_imagebuilder.types.non_empty_string


class ListContainerRecipesResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    container_recipe_summary_list: NotRequired[
        "capo_imagebuilder.types.container_recipe_summary_list.ContainerRecipeSummaryList"
    ]
    """<p>The list of container recipes returned for the request.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContainerRecipesResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "container_recipe_summary_list" in value:
        import capo_imagebuilder.types.container_recipe_summary_list

        out["containerRecipeSummaryList"] = (
            capo_imagebuilder.types.container_recipe_summary_list.serialize_json(
                value["container_recipe_summary_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContainerRecipesResponse:
    out: ListContainerRecipesResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "containerRecipeSummaryList" in data:
        import capo_imagebuilder.types.container_recipe_summary_list

        out["container_recipe_summary_list"] = (
            capo_imagebuilder.types.container_recipe_summary_list.deserialize_json(
                data["containerRecipeSummaryList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
