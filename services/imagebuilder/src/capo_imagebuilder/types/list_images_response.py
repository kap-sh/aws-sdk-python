"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_version_list
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.pagination_token


class ListImagesResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    image_version_list: NotRequired[
        "capo_imagebuilder.types.image_version_list.ImageVersionList"
    ]
    """<p>The list of image semantic versions.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Filtering:</b> With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.</p> </note>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImagesResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "image_version_list" in value:
        import capo_imagebuilder.types.image_version_list

        out["imageVersionList"] = (
            capo_imagebuilder.types.image_version_list.serialize_json(
                value["image_version_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImagesResponse:
    out: ListImagesResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "imageVersionList" in data:
        import capo_imagebuilder.types.image_version_list

        out["image_version_list"] = (
            capo_imagebuilder.types.image_version_list.deserialize_json(
                data["imageVersionList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
