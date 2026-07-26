"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.system_event_metadata


class SystemEventDetails(TypedDict, closed=True):
    title: "str"
    """<p>The title of the event.</p>"""
    description: "str"
    """<p>The description of the event.</p>"""
    event_metadata: NotRequired[
        "capo_resiliencehubv2.types.system_event_metadata.SystemEventMetadata"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SystemEventDetails) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["description"] = value["description"]
    if "event_metadata" in value:
        import capo_resiliencehubv2.types.system_event_metadata

        out["eventMetadata"] = (
            capo_resiliencehubv2.types.system_event_metadata.serialize_json(
                value["event_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> SystemEventDetails:
    out: SystemEventDetails = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("SystemEventDetails.title required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("SystemEventDetails.description required")
    if "eventMetadata" in data:
        import capo_resiliencehubv2.types.system_event_metadata

        out["event_metadata"] = (
            capo_resiliencehubv2.types.system_event_metadata.deserialize_json(
                data["eventMetadata"]
            )
        )
    return out
