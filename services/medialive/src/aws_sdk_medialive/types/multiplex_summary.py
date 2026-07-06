"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.multiplex_settings_summary
    import aws_sdk_medialive.types.multiplex_state
    import aws_sdk_medialive.types.tags


class MultiplexSummary(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The unique arn of the multiplex."""
    availability_zones: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of availability zones for the multiplex."""
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The unique id of the multiplex."""
    multiplex_settings: NotRequired[
        "aws_sdk_medialive.types.multiplex_settings_summary.MultiplexSettingsSummary"
    ]
    """Configuration for a multiplex event."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name of the multiplex."""
    pipelines_running_count: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """The number of currently healthy pipelines."""
    program_count: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """The number of programs in the multiplex."""
    state: NotRequired["aws_sdk_medialive.types.multiplex_state.MultiplexState"]
    """The current state of the multiplex."""
    tags: NotRequired["aws_sdk_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "availability_zones" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["availabilityZones"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["availability_zones"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "multiplex_settings" in value:
        import aws_sdk_medialive.types.multiplex_settings_summary

        out["multiplexSettings"] = (
            aws_sdk_medialive.types.multiplex_settings_summary.serialize_json(
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
        import aws_sdk_medialive.types.multiplex_state

        out["state"] = aws_sdk_medialive.types.multiplex_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> MultiplexSummary:
    out: MultiplexSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "availabilityZones" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["availability_zones"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["availabilityZones"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "multiplexSettings" in data:
        import aws_sdk_medialive.types.multiplex_settings_summary

        out["multiplex_settings"] = (
            aws_sdk_medialive.types.multiplex_settings_summary.deserialize_json(
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
        import aws_sdk_medialive.types.multiplex_state

        out["state"] = aws_sdk_medialive.types.multiplex_state.deserialize_json(
            data["state"]
        )
    if "tags" in data:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.deserialize_json(data["tags"])
    return out
