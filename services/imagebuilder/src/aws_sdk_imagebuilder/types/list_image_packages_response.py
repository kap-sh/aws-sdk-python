"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImagePackagesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_package_list
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.pagination_token


class ListImagePackagesResponse(TypedDict):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    image_package_list: NotRequired[
        "aws_sdk_imagebuilder.types.image_package_list.ImagePackageList"
    ]
    """<p>The list of Image Packages returned in the response.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImagePackagesResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "image_package_list" in value:
        import aws_sdk_imagebuilder.types.image_package_list

        out["imagePackageList"] = (
            aws_sdk_imagebuilder.types.image_package_list.serialize_json(
                value["image_package_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImagePackagesResponse:
    out: ListImagePackagesResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "imagePackageList" in data:
        import aws_sdk_imagebuilder.types.image_package_list

        out["image_package_list"] = (
            aws_sdk_imagebuilder.types.image_package_list.deserialize_json(
                data["imagePackageList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
