"""Generated from Smithy shape ``com.amazonaws.medialive#CreateMultiplexRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.multiplex_settings
    import aws_sdk_medialive.types.tags


class CreateMultiplexRequest(TypedDict):
    availability_zones: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of availability zones for the multiplex. You must specify exactly two."""
    multiplex_settings: NotRequired[
        "aws_sdk_medialive.types.multiplex_settings.MultiplexSettings"
    ]
    """Configuration for a multiplex event."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Name of multiplex."""
    request_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Unique request ID. This prevents retries from creating multiple resources."""
    tags: NotRequired["aws_sdk_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMultiplexRequest) -> dict:
    out: dict = {}
    if "availability_zones" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["availabilityZones"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["availability_zones"]
            )
        )
    if "multiplex_settings" in value:
        import aws_sdk_medialive.types.multiplex_settings

        out["multiplexSettings"] = (
            aws_sdk_medialive.types.multiplex_settings.serialize_json(
                value["multiplex_settings"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "tags" in value:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMultiplexRequest:
    out: CreateMultiplexRequest = {}  # type: ignore[typeddict-item]
    if "availabilityZones" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["availability_zones"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["availabilityZones"]
            )
        )
    if "multiplexSettings" in data:
        import aws_sdk_medialive.types.multiplex_settings

        out["multiplex_settings"] = (
            aws_sdk_medialive.types.multiplex_settings.deserialize_json(
                data["multiplexSettings"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "tags" in data:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.deserialize_json(data["tags"])
    return out
