"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImagePipelineImagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_summary_list
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.pagination_token


class ListImagePipelineImagesResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    image_summary_list: NotRequired[
        "capo_imagebuilder.types.image_summary_list.ImageSummaryList"
    ]
    """<p>The list of images built by this pipeline.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImagePipelineImagesResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "image_summary_list" in value:
        import capo_imagebuilder.types.image_summary_list

        out["imageSummaryList"] = (
            capo_imagebuilder.types.image_summary_list.serialize_json(
                value["image_summary_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImagePipelineImagesResponse:
    out: ListImagePipelineImagesResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "imageSummaryList" in data:
        import capo_imagebuilder.types.image_summary_list

        out["image_summary_list"] = (
            capo_imagebuilder.types.image_summary_list.deserialize_json(
                data["imageSummaryList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
