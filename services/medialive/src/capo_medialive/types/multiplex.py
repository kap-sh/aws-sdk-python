"""Generated from Smithy shape ``com.amazonaws.medialive#Multiplex``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer
    import capo_medialive.types.__list_of__string
    import capo_medialive.types.__list_of_multiplex_output_destination
    import capo_medialive.types.__string
    import capo_medialive.types.multiplex_settings
    import capo_medialive.types.multiplex_state
    import capo_medialive.types.tags


class Multiplex(TypedDict, closed=True):
    arn: NotRequired["capo_medialive.types.__string.__string"]
    """The unique arn of the multiplex."""
    availability_zones: NotRequired[
        "capo_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of availability zones for the multiplex."""
    destinations: NotRequired[
        "capo_medialive.types.__list_of_multiplex_output_destination.__listOfMultiplexOutputDestination"
    ]
    """A list of the multiplex output destinations."""
    id: NotRequired["capo_medialive.types.__string.__string"]
    """The unique id of the multiplex."""
    multiplex_settings: NotRequired[
        "capo_medialive.types.multiplex_settings.MultiplexSettings"
    ]
    """Configuration for a multiplex event."""
    name: NotRequired["capo_medialive.types.__string.__string"]
    """The name of the multiplex."""
    pipelines_running_count: NotRequired["capo_medialive.types.__integer.__integer"]
    """The number of currently healthy pipelines."""
    program_count: NotRequired["capo_medialive.types.__integer.__integer"]
    """The number of programs in the multiplex."""
    state: NotRequired["capo_medialive.types.multiplex_state.MultiplexState"]
    """The current state of the multiplex."""
    tags: NotRequired["capo_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""


# --- restJson1 ser/de ---
def serialize_json(value: Multiplex) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "availability_zones" in value:
        import capo_medialive.types.__list_of__string

        out["availabilityZones"] = (
            capo_medialive.types.__list_of__string.serialize_json(
                value["availability_zones"]
            )
        )
    if "destinations" in value:
        import capo_medialive.types.__list_of_multiplex_output_destination

        out["destinations"] = (
            capo_medialive.types.__list_of_multiplex_output_destination.serialize_json(
                value["destinations"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "multiplex_settings" in value:
        import capo_medialive.types.multiplex_settings

        out["multiplexSettings"] = (
            capo_medialive.types.multiplex_settings.serialize_json(
                value["multiplex_settings"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "pipelines_running_count" in value:
        out["pipelinesRunningCount"] = value["pipelines_running_count"]
    if "program_count" in value:
        out["programCount"] = value["program_count"]
    if "state" in value:
        import capo_medialive.types.multiplex_state

        out["state"] = capo_medialive.types.multiplex_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Multiplex:
    out: Multiplex = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "availabilityZones" in data:
        import capo_medialive.types.__list_of__string

        out["availability_zones"] = (
            capo_medialive.types.__list_of__string.deserialize_json(
                data["availabilityZones"]
            )
        )
    if "destinations" in data:
        import capo_medialive.types.__list_of_multiplex_output_destination

        out["destinations"] = (
            capo_medialive.types.__list_of_multiplex_output_destination.deserialize_json(
                data["destinations"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "multiplexSettings" in data:
        import capo_medialive.types.multiplex_settings

        out["multiplex_settings"] = (
            capo_medialive.types.multiplex_settings.deserialize_json(
                data["multiplexSettings"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "pipelinesRunningCount" in data:
        out["pipelines_running_count"] = data["pipelinesRunningCount"]
    if "programCount" in data:
        out["program_count"] = data["programCount"]
    if "state" in data:
        import capo_medialive.types.multiplex_state

        out["state"] = capo_medialive.types.multiplex_state.deserialize_json(
            data["state"]
        )
    if "tags" in data:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.deserialize_json(data["tags"])
    return out
