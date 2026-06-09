"""Generated from Smithy shape ``com.amazonaws.lambda#ListEventSourceMappingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.event_source_mappings_list
    import aws_sdk_lambda.types.string


class ListEventSourceMappingsResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>A pagination token that's returned when the response doesn't contain all event source mappings.</p>"""
    event_source_mappings: NotRequired[
        "aws_sdk_lambda.types.event_source_mappings_list.EventSourceMappingsList"
    ]
    """<p>A list of event source mappings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventSourceMappingsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "event_source_mappings" in value:
        import aws_sdk_lambda.types.event_source_mappings_list

        out["EventSourceMappings"] = (
            aws_sdk_lambda.types.event_source_mappings_list.serialize_json(
                value["event_source_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListEventSourceMappingsResponse:
    out: ListEventSourceMappingsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "EventSourceMappings" in data:
        import aws_sdk_lambda.types.event_source_mappings_list

        out["event_source_mappings"] = (
            aws_sdk_lambda.types.event_source_mappings_list.deserialize_json(
                data["EventSourceMappings"]
            )
        )
    return out
