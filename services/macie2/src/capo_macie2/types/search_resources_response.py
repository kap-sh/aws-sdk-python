"""Generated from Smithy shape ``com.amazonaws.macie2#SearchResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_matching_resource
    import capo_macie2.types.__string


class SearchResourcesResponse(TypedDict, closed=True):
    matching_resources: NotRequired[
        "capo_macie2.types.__list_of_matching_resource.__listOfMatchingResource"
    ]
    """<p>An array of objects, one for each resource that matches the filter criteria specified in the request.</p>"""
    next_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesResponse) -> dict:
    out: dict = {}
    if "matching_resources" in value:
        import capo_macie2.types.__list_of_matching_resource

        out["matchingResources"] = (
            capo_macie2.types.__list_of_matching_resource.serialize_json(
                value["matching_resources"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchResourcesResponse:
    out: SearchResourcesResponse = {}  # type: ignore[typeddict-item]
    if "matchingResources" in data:
        import capo_macie2.types.__list_of_matching_resource

        out["matching_resources"] = (
            capo_macie2.types.__list_of_matching_resource.deserialize_json(
                data["matchingResources"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
