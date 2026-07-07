"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImageBuildVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.filter_list
    import aws_sdk_imagebuilder.types.image_version_arn
    import aws_sdk_imagebuilder.types.pagination_token
    import aws_sdk_imagebuilder.types.restricted_integer


class ListImageBuildVersionsRequest(TypedDict, closed=True):
    image_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_version_arn.ImageVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image whose build versions you want to retrieve.</p>"""
    filters: NotRequired["aws_sdk_imagebuilder.types.filter_list.FilterList"]
    """<p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>osVersion</code> </p> </li> <li> <p> <code>platform</code> </p> </li> <li> <p> <code>type</code> </p> </li> <li> <p> <code>version</code> </p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>Specify the maximum number of items to return in a request.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImageBuildVersionsRequest) -> dict:
    out: dict = {}
    if "image_version_arn" in value:
        out["imageVersionArn"] = value["image_version_arn"]
    if "filters" in value:
        import aws_sdk_imagebuilder.types.filter_list

        out["filters"] = aws_sdk_imagebuilder.types.filter_list.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImageBuildVersionsRequest:
    out: ListImageBuildVersionsRequest = {}  # type: ignore[typeddict-item]
    if "imageVersionArn" in data:
        out["image_version_arn"] = data["imageVersionArn"]
    if "filters" in data:
        import aws_sdk_imagebuilder.types.filter_list

        out["filters"] = aws_sdk_imagebuilder.types.filter_list.deserialize_json(
            data["filters"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
