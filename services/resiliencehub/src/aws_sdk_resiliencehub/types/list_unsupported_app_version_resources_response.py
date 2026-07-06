"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListUnsupportedAppVersionResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.next_token
    import aws_sdk_resiliencehub.types.string255
    import aws_sdk_resiliencehub.types.unsupported_resource_list


class ListUnsupportedAppVersionResourcesResponse(TypedDict, closed=True):
    unsupported_resources: (
        "aws_sdk_resiliencehub.types.unsupported_resource_list.UnsupportedResourceList"
    )
    """<p>The unsupported resources for the application.</p>"""
    resolution_id: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>The identifier for a specific resolution.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUnsupportedAppVersionResourcesResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehub.types.unsupported_resource_list

    out["unsupportedResources"] = (
        aws_sdk_resiliencehub.types.unsupported_resource_list.serialize_json(
            value["unsupported_resources"]
        )
    )
    out["resolutionId"] = value["resolution_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUnsupportedAppVersionResourcesResponse:
    out: ListUnsupportedAppVersionResourcesResponse = {}  # type: ignore[typeddict-item]
    if "unsupportedResources" in data:
        import aws_sdk_resiliencehub.types.unsupported_resource_list

        out["unsupported_resources"] = (
            aws_sdk_resiliencehub.types.unsupported_resource_list.deserialize_json(
                data["unsupportedResources"]
            )
        )
    else:
        raise DeserializationError(
            "ListUnsupportedAppVersionResourcesResponse.unsupported_resources required"
        )
    if "resolutionId" in data:
        out["resolution_id"] = data["resolutionId"]
    else:
        raise DeserializationError(
            "ListUnsupportedAppVersionResourcesResponse.resolution_id required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
