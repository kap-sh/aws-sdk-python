"""Generated from Smithy shape ``com.amazonaws.lambda#ListEventSourceMappingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.event_source_mappings_list
    import capo_lambda.types.string


class ListEventSourceMappingsResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>A pagination token that's returned when the response doesn't contain all event source mappings.</p>"""
    event_source_mappings: NotRequired[
        "capo_lambda.types.event_source_mappings_list.EventSourceMappingsList"
    ]
    """<p>A list of event source mappings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventSourceMappingsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "event_source_mappings" in value:
        import capo_lambda.types.event_source_mappings_list

        out["EventSourceMappings"] = (
            capo_lambda.types.event_source_mappings_list.serialize_json(
                value["event_source_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListEventSourceMappingsResponse:
    out: ListEventSourceMappingsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "EventSourceMappings" in data:
        import capo_lambda.types.event_source_mappings_list

        out["event_source_mappings"] = (
            capo_lambda.types.event_source_mappings_list.deserialize_json(
                data["EventSourceMappings"]
            )
        )
    return out
