"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#BatchUpdateAttendeeCapabilitiesExceptRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.attendee_capabilities
    import aws_sdk_chime_sdk_meetings.types.attendee_ids_list
    import aws_sdk_chime_sdk_meetings.types.guid_string


class BatchUpdateAttendeeCapabilitiesExceptRequest(TypedDict):
    meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The ID of the meeting associated with the update request.</p>"""
    excluded_attendee_ids: (
        "aws_sdk_chime_sdk_meetings.types.attendee_ids_list.AttendeeIdsList"
    )
    """<p>The <code>AttendeeIDs</code> that you want to exclude from one or more capabilities.</p>"""
    capabilities: (
        "aws_sdk_chime_sdk_meetings.types.attendee_capabilities.AttendeeCapabilities"
    )
    """<p>The capabilities (<code>audio</code>, <code>video</code>, or <code>content</code>) that you want to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateAttendeeCapabilitiesExceptRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_meetings.types.attendee_ids_list

    out["ExcludedAttendeeIds"] = (
        aws_sdk_chime_sdk_meetings.types.attendee_ids_list.serialize_json(
            value["excluded_attendee_ids"]
        )
    )
    import aws_sdk_chime_sdk_meetings.types.attendee_capabilities

    out["Capabilities"] = (
        aws_sdk_chime_sdk_meetings.types.attendee_capabilities.serialize_json(
            value["capabilities"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateAttendeeCapabilitiesExceptRequest:
    out: BatchUpdateAttendeeCapabilitiesExceptRequest = {}  # type: ignore[typeddict-item]
    if "ExcludedAttendeeIds" in data:
        import aws_sdk_chime_sdk_meetings.types.attendee_ids_list

        out["excluded_attendee_ids"] = (
            aws_sdk_chime_sdk_meetings.types.attendee_ids_list.deserialize_json(
                data["ExcludedAttendeeIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateAttendeeCapabilitiesExceptRequest.excluded_attendee_ids required"
        )
    if "Capabilities" in data:
        import aws_sdk_chime_sdk_meetings.types.attendee_capabilities

        out["capabilities"] = (
            aws_sdk_chime_sdk_meetings.types.attendee_capabilities.deserialize_json(
                data["Capabilities"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateAttendeeCapabilitiesExceptRequest.capabilities required"
        )
    return out
