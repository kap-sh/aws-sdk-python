"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#UpdateAttendeeCapabilitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_meetings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.attendee_capabilities
    import capo_chime_sdk_meetings.types.guid_string


class UpdateAttendeeCapabilitiesRequest(TypedDict, closed=True):
    meeting_id: "capo_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The ID of the meeting associated with the update request.</p>"""
    attendee_id: "capo_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The ID of the attendee associated with the update request.</p>"""
    capabilities: (
        "capo_chime_sdk_meetings.types.attendee_capabilities.AttendeeCapabilities"
    )
    """<p>The capabilities that you want to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAttendeeCapabilitiesRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_meetings.types.attendee_capabilities

    out["Capabilities"] = (
        capo_chime_sdk_meetings.types.attendee_capabilities.serialize_json(
            value["capabilities"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAttendeeCapabilitiesRequest:
    out: UpdateAttendeeCapabilitiesRequest = {}  # type: ignore[typeddict-item]
    if "Capabilities" in data:
        import capo_chime_sdk_meetings.types.attendee_capabilities

        out["capabilities"] = (
            capo_chime_sdk_meetings.types.attendee_capabilities.deserialize_json(
                data["Capabilities"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAttendeeCapabilitiesRequest.capabilities required"
        )
    return out
