"""Generated from Smithy shape ``com.amazonaws.medialive#MediaResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_media_resource_neighbor
    import aws_sdk_medialive.types.__string_min1_max256


class MediaResource(TypedDict):
    destinations: NotRequired[
        "aws_sdk_medialive.types.__list_of_media_resource_neighbor.__listOfMediaResourceNeighbor"
    ]
    name: NotRequired["aws_sdk_medialive.types.__string_min1_max256.__stringMin1Max256"]
    """The logical name of an AWS media resource."""
    sources: NotRequired[
        "aws_sdk_medialive.types.__list_of_media_resource_neighbor.__listOfMediaResourceNeighbor"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MediaResource) -> dict:
    out: dict = {}
    if "destinations" in value:
        import aws_sdk_medialive.types.__list_of_media_resource_neighbor

        out["destinations"] = (
            aws_sdk_medialive.types.__list_of_media_resource_neighbor.serialize_json(
                value["destinations"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "sources" in value:
        import aws_sdk_medialive.types.__list_of_media_resource_neighbor

        out["sources"] = (
            aws_sdk_medialive.types.__list_of_media_resource_neighbor.serialize_json(
                value["sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaResource:
    out: MediaResource = {}  # type: ignore[typeddict-item]
    if "destinations" in data:
        import aws_sdk_medialive.types.__list_of_media_resource_neighbor

        out["destinations"] = (
            aws_sdk_medialive.types.__list_of_media_resource_neighbor.deserialize_json(
                data["destinations"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "sources" in data:
        import aws_sdk_medialive.types.__list_of_media_resource_neighbor

        out["sources"] = (
            aws_sdk_medialive.types.__list_of_media_resource_neighbor.deserialize_json(
                data["sources"]
            )
        )
    return out
