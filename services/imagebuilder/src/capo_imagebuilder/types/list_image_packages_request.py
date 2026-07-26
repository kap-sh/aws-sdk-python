"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImagePackagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_build_version_arn
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.restricted_integer


class ListImagePackagesRequest(TypedDict, closed=True):
    image_build_version_arn: (
        "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    )
    """<p>Filter results for the ListImagePackages request by the Image Build Version ARN</p>"""
    max_results: NotRequired[
        "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>Specify the maximum number of items to return in a request.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImagePackagesRequest) -> dict:
    out: dict = {}
    out["imageBuildVersionArn"] = value["image_build_version_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImagePackagesRequest:
    out: ListImagePackagesRequest = {}  # type: ignore[typeddict-item]
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    else:
        raise DeserializationError(
            "ListImagePackagesRequest.image_build_version_arn required"
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
