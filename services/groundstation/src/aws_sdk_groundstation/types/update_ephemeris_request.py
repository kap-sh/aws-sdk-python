"""Generated from Smithy shape ``com.amazonaws.groundstation#UpdateEphemerisRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.ephemeris_priority
    import aws_sdk_groundstation.types.safe_name
    import aws_sdk_groundstation.types.uuid


class UpdateEphemerisRequest(TypedDict):
    ephemeris_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>The AWS Ground Station ephemeris ID.</p>"""
    enabled: "bool"
    """<p>Enable or disable the ephemeris. Changing this value doesn't require re-validation.</p>"""
    name: NotRequired["aws_sdk_groundstation.types.safe_name.SafeName"]
    """<p>A name that you can use to identify the ephemeris.</p>"""
    priority: NotRequired[
        "aws_sdk_groundstation.types.ephemeris_priority.EphemerisPriority"
    ]
    """<p>A priority score that determines which ephemeris to use when multiple ephemerides overlap.</p> <p>Higher numbers take precedence. The default is 1. Must be 1 or greater.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEphemerisRequest) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    if "name" in value:
        out["name"] = value["name"]
    if "priority" in value:
        out["priority"] = value["priority"]
    return out


def deserialize_json(data: dict) -> UpdateEphemerisRequest:
    out: UpdateEphemerisRequest = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        raise DeserializationError("UpdateEphemerisRequest.enabled required")
    if "name" in data:
        out["name"] = data["name"]
    if "priority" in data:
        out["priority"] = data["priority"]
    return out
