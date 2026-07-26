"""Generated from Smithy shape ``com.amazonaws.medialive#CreateMultiplexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of__string
    import capo_medialive.types.__string
    import capo_medialive.types.multiplex_settings
    import capo_medialive.types.tags


class CreateMultiplexRequest(TypedDict, closed=True):
    availability_zones: NotRequired[
        "capo_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of availability zones for the multiplex. You must specify exactly two."""
    multiplex_settings: NotRequired[
        "capo_medialive.types.multiplex_settings.MultiplexSettings"
    ]
    """Configuration for a multiplex event."""
    name: NotRequired["capo_medialive.types.__string.__string"]
    """Name of multiplex."""
    request_id: NotRequired["capo_medialive.types.__string.__string"]
    """Unique request ID. This prevents retries from creating multiple resources."""
    tags: NotRequired["capo_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMultiplexRequest) -> dict:
    out: dict = {}
    if "availability_zones" in value:
        import capo_medialive.types.__list_of__string

        out["availabilityZones"] = (
            capo_medialive.types.__list_of__string.serialize_json(
                value["availability_zones"]
            )
        )
    if "multiplex_settings" in value:
        import capo_medialive.types.multiplex_settings

        out["multiplexSettings"] = (
            capo_medialive.types.multiplex_settings.serialize_json(
                value["multiplex_settings"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "tags" in value:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMultiplexRequest:
    out: CreateMultiplexRequest = {}  # type: ignore[typeddict-item]
    if "availabilityZones" in data:
        import capo_medialive.types.__list_of__string

        out["availability_zones"] = (
            capo_medialive.types.__list_of__string.deserialize_json(
                data["availabilityZones"]
            )
        )
    if "multiplexSettings" in data:
        import capo_medialive.types.multiplex_settings

        out["multiplex_settings"] = (
            capo_medialive.types.multiplex_settings.deserialize_json(
                data["multiplexSettings"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "tags" in data:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.deserialize_json(data["tags"])
    return out
