"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppVersionResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.next_token
    import capo_resiliencehub.types.physical_resource_list
    import capo_resiliencehub.types.string255


class ListAppVersionResourcesResponse(TypedDict, closed=True):
    physical_resources: (
        "capo_resiliencehub.types.physical_resource_list.PhysicalResourceList"
    )
    """<p>The physical resources in the application version.</p>"""
    resolution_id: "capo_resiliencehub.types.string255.String255"
    """<p>The ID for a specific resolution.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppVersionResourcesResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.physical_resource_list

    out["physicalResources"] = (
        capo_resiliencehub.types.physical_resource_list.serialize_json(
            value["physical_resources"]
        )
    )
    out["resolutionId"] = value["resolution_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppVersionResourcesResponse:
    out: ListAppVersionResourcesResponse = {}  # type: ignore[typeddict-item]
    if "physicalResources" in data:
        import capo_resiliencehub.types.physical_resource_list

        out["physical_resources"] = (
            capo_resiliencehub.types.physical_resource_list.deserialize_json(
                data["physicalResources"]
            )
        )
    else:
        raise DeserializationError(
            "ListAppVersionResourcesResponse.physical_resources required"
        )
    if "resolutionId" in data:
        out["resolution_id"] = data["resolutionId"]
    else:
        raise DeserializationError(
            "ListAppVersionResourcesResponse.resolution_id required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
