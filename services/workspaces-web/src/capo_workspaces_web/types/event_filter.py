"""Generated from Smithy shape ``com.amazonaws.workspacesweb#EventFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_workspaces_web.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.events


class _EventFilter_all(TypedDict, closed=True):
    all: "None"


class _EventFilter_include(TypedDict, closed=True):
    include: "capo_workspaces_web.types.events.Events"


EventFilter: TypeAlias = _EventFilter_all | _EventFilter_include


# --- restJson1 ser/de ---
def serialize_json(value: EventFilter) -> dict:
    if "all" in value:
        return {"all": {}}
    elif "include" in value:
        import capo_workspaces_web.types.events

        return {
            "include": capo_workspaces_web.types.events.serialize_json(value["include"])
        }
    else:
        raise SerializationError("EventFilter: no variant present")


def deserialize_json(data: dict) -> EventFilter:
    if "all" in data:
        return {"all": None}
    elif "include" in data:
        import capo_workspaces_web.types.events

        return {
            "include": capo_workspaces_web.types.events.deserialize_json(
                data["include"]
            )
        }
    else:
        raise DeserializationError("EventFilter: no recognized variant key")
