"""Generated from Smithy shape ``com.amazonaws.medialive#MediaResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_media_resource_neighbor
    import capo_medialive.types.__string_min1_max256


class MediaResource(TypedDict, closed=True):
    destinations: NotRequired[
        "capo_medialive.types.__list_of_media_resource_neighbor.__listOfMediaResourceNeighbor"
    ]
    name: NotRequired["capo_medialive.types.__string_min1_max256.__stringMin1Max256"]
    """The logical name of an AWS media resource."""
    sources: NotRequired[
        "capo_medialive.types.__list_of_media_resource_neighbor.__listOfMediaResourceNeighbor"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MediaResource) -> dict:
    out: dict = {}
    if "destinations" in value:
        import capo_medialive.types.__list_of_media_resource_neighbor

        out["destinations"] = (
            capo_medialive.types.__list_of_media_resource_neighbor.serialize_json(
                value["destinations"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "sources" in value:
        import capo_medialive.types.__list_of_media_resource_neighbor

        out["sources"] = (
            capo_medialive.types.__list_of_media_resource_neighbor.serialize_json(
                value["sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaResource:
    out: MediaResource = {}  # type: ignore[typeddict-item]
    if "destinations" in data:
        import capo_medialive.types.__list_of_media_resource_neighbor

        out["destinations"] = (
            capo_medialive.types.__list_of_media_resource_neighbor.deserialize_json(
                data["destinations"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "sources" in data:
        import capo_medialive.types.__list_of_media_resource_neighbor

        out["sources"] = (
            capo_medialive.types.__list_of_media_resource_neighbor.deserialize_json(
                data["sources"]
            )
        )
    return out
