"""Generated from Smithy shape ``com.amazonaws.appintegrations#EventFilter``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_appintegrations.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.source

class EventFilter(TypedDict):
    source: "aws_sdk_appintegrations.types.source.Source"
    """<p>The source of the events.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: EventFilter) -> dict:
    out: dict = {}
    out["Source"] = value["source"]
    return out


def deserialize_json(data: dict) -> EventFilter:
    out: EventFilter = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        out["source"] = data["Source"]
    else:
        raise DeserializationError("EventFilter.source required")
    return out