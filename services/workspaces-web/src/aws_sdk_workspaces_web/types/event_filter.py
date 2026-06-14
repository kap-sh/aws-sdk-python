"""Generated from Smithy shape ``com.amazonaws.workspacesweb#EventFilter``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.events


class _EventFilter_all(TypedDict):
    all: "None"


class _EventFilter_include(TypedDict):
    include: "aws_sdk_workspaces_web.types.events.Events"


EventFilter: TypeAlias = _EventFilter_all | _EventFilter_include


# --- restJson1 ser/de ---
def serialize_json(value: EventFilter) -> dict:
    if "all" in value:
        return {"all": {}}
    elif "include" in value:
        import aws_sdk_workspaces_web.types.events

        return {
            "include": aws_sdk_workspaces_web.types.events.serialize_json(
                value["include"]
            )
        }
    else:
        raise SerializationError("EventFilter: no variant present")


def deserialize_json(data: dict) -> EventFilter:
    if "all" in data:
        return {"all": None}
    elif "include" in data:
        import aws_sdk_workspaces_web.types.events

        return {
            "include": aws_sdk_workspaces_web.types.events.deserialize_json(
                data["include"]
            )
        }
    else:
        raise DeserializationError("EventFilter: no recognized variant key")
