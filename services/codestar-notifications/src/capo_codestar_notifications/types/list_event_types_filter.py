"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListEventTypesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codestar_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codestar_notifications.types.list_event_types_filter_name
    import capo_codestar_notifications.types.list_event_types_filter_value


class ListEventTypesFilter(TypedDict, closed=True):
    name: "capo_codestar_notifications.types.list_event_types_filter_name.ListEventTypesFilterName"
    """<p>The system-generated name of the filter type you want to filter by.</p>"""
    value: "capo_codestar_notifications.types.list_event_types_filter_value.ListEventTypesFilterValue"
    """<p>The name of the resource type (for example, pipeline) or service name (for example, CodePipeline) that you want to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventTypesFilter) -> dict:
    out: dict = {}
    import capo_codestar_notifications.types.list_event_types_filter_name

    out["Name"] = (
        capo_codestar_notifications.types.list_event_types_filter_name.serialize_json(
            value["name"]
        )
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ListEventTypesFilter:
    out: ListEventTypesFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import capo_codestar_notifications.types.list_event_types_filter_name

        out["name"] = (
            capo_codestar_notifications.types.list_event_types_filter_name.deserialize_json(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("ListEventTypesFilter.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("ListEventTypesFilter.value required")
    return out
