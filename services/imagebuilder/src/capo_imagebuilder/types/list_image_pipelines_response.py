"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImagePipelinesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_pipeline_list
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.pagination_token


class ListImagePipelinesResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    image_pipeline_list: NotRequired[
        "capo_imagebuilder.types.image_pipeline_list.ImagePipelineList"
    ]
    """<p>The list of image pipelines.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImagePipelinesResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "image_pipeline_list" in value:
        import capo_imagebuilder.types.image_pipeline_list

        out["imagePipelineList"] = (
            capo_imagebuilder.types.image_pipeline_list.serialize_json(
                value["image_pipeline_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImagePipelinesResponse:
    out: ListImagePipelinesResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "imagePipelineList" in data:
        import capo_imagebuilder.types.image_pipeline_list

        out["image_pipeline_list"] = (
            capo_imagebuilder.types.image_pipeline_list.deserialize_json(
                data["imagePipelineList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
