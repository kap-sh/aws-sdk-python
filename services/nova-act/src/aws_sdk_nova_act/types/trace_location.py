"""Generated from Smithy shape ``com.amazonaws.novaact#TraceLocation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.non_blank_string
    import aws_sdk_nova_act.types.trace_location_type


class TraceLocation(TypedDict):
    location_type: "aws_sdk_nova_act.types.trace_location_type.TraceLocationType"
    """<p>The type of storage location for the trace data.</p>"""
    location: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>The specific location where the trace data is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TraceLocation) -> dict:
    out: dict = {}
    import aws_sdk_nova_act.types.trace_location_type

    out["locationType"] = aws_sdk_nova_act.types.trace_location_type.serialize_json(
        value["location_type"]
    )
    out["location"] = value["location"]
    return out


def deserialize_json(data: dict) -> TraceLocation:
    out: TraceLocation = {}  # type: ignore[typeddict-item]
    if "locationType" in data:
        import aws_sdk_nova_act.types.trace_location_type

        out["location_type"] = (
            aws_sdk_nova_act.types.trace_location_type.deserialize_json(
                data["locationType"]
            )
        )
    else:
        raise DeserializationError("TraceLocation.location_type required")
    if "location" in data:
        out["location"] = data["location"]
    else:
        raise DeserializationError("TraceLocation.location required")
    return out
