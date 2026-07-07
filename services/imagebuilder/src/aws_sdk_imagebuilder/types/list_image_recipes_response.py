"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImageRecipesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_recipe_summary_list
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.pagination_token


class ListImageRecipesResponse(TypedDict, closed=True):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    image_recipe_summary_list: NotRequired[
        "aws_sdk_imagebuilder.types.image_recipe_summary_list.ImageRecipeSummaryList"
    ]
    """<p>A list of <code>ImageRecipeSummary</code> objects that contain identifying characteristics for the image recipe, such as the name, the Amazon Resource Name (ARN), and the date created, along with other key details.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImageRecipesResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "image_recipe_summary_list" in value:
        import aws_sdk_imagebuilder.types.image_recipe_summary_list

        out["imageRecipeSummaryList"] = (
            aws_sdk_imagebuilder.types.image_recipe_summary_list.serialize_json(
                value["image_recipe_summary_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImageRecipesResponse:
    out: ListImageRecipesResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "imageRecipeSummaryList" in data:
        import aws_sdk_imagebuilder.types.image_recipe_summary_list

        out["image_recipe_summary_list"] = (
            aws_sdk_imagebuilder.types.image_recipe_summary_list.deserialize_json(
                data["imageRecipeSummaryList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
