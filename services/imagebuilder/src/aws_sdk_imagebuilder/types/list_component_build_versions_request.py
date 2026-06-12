"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListComponentBuildVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_version_arn
    import aws_sdk_imagebuilder.types.pagination_token
    import aws_sdk_imagebuilder.types.restricted_integer


class ListComponentBuildVersionsRequest(TypedDict):
    component_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.component_version_arn.ComponentVersionArn"
    ]
    """<p>The component version Amazon Resource Name (ARN) whose versions you want to list.</p>"""
    max_results: NotRequired[
        "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>Specify the maximum number of items to return in a request.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentBuildVersionsRequest) -> dict:
    out: dict = {}
    if "component_version_arn" in value:
        out["componentVersionArn"] = value["component_version_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComponentBuildVersionsRequest:
    out: ListComponentBuildVersionsRequest = {}  # type: ignore[typeddict-item]
    if "componentVersionArn" in data:
        out["component_version_arn"] = data["componentVersionArn"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
