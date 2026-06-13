"""Generated from Smithy shape ``com.amazonaws.rum#RumEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rum.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_rum.types.json_value


class RumEvent(TypedDict):
    id: "str"
    """<p>A unique ID for this event.</p>"""
    timestamp: "datetime.datetime"
    """<p>The exact time that this event occurred.</p>"""
    type: "str"
    """<p>The JSON schema that denotes the type of event this is, such as a page load or a new session.</p>"""
    metadata: NotRequired["aws_sdk_rum.types.json_value.JsonValue"]
    """<p>Metadata about this event, which contains a JSON serialization of the identity of the user for this session. The user information comes from information such as the HTTP user-agent request header and document interface.</p>"""
    details: "aws_sdk_rum.types.json_value.JsonValue"
    """<p>A string containing details about the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RumEvent) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_rum.types._prelude.timestamp

    out["timestamp"] = aws_sdk_rum.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    out["type"] = value["type"]
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    out["details"] = value["details"]
    return out


def deserialize_json(data: dict) -> RumEvent:
    out: RumEvent = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("RumEvent.id required")
    if "timestamp" in data:
        import aws_sdk_rum.types._prelude.timestamp

        out["timestamp"] = aws_sdk_rum.types._prelude.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError("RumEvent.timestamp required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("RumEvent.type required")
    if "metadata" in data:
        out["metadata"] = data["metadata"]
    if "details" in data:
        out["details"] = data["details"]
    else:
        raise DeserializationError("RumEvent.details required")
    return out
