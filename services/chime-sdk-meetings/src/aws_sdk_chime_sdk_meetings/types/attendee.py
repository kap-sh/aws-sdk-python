"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#Attendee``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.attendee_capabilities
    import aws_sdk_chime_sdk_meetings.types.external_user_id
    import aws_sdk_chime_sdk_meetings.types.guid_string
    import aws_sdk_chime_sdk_meetings.types.join_token_string


class Attendee(TypedDict):
    external_user_id: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.external_user_id.ExternalUserId"
    ]
    r"""<p>The Amazon Chime SDK external user ID. An idempotency token. Links the attendee to an identity managed by a builder application.</p> <p>Pattern: <code>[-_&@+=,(){}\[\]\/«».:|'\"#a-zA-Z0-9À-ÿ\s]*</code> </p> <p>Values that begin with <code>aws:</code> are reserved. You can't configure a value that uses this prefix. Case insensitive.</p>"""
    attendee_id: NotRequired["aws_sdk_chime_sdk_meetings.types.guid_string.GuidString"]
    """<p>The Amazon Chime SDK attendee ID.</p>"""
    join_token: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.join_token_string.JoinTokenString"
    ]
    """<p>The join token used by the Amazon Chime SDK attendee.</p>"""
    capabilities: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.attendee_capabilities.AttendeeCapabilities"
    ]
    """<p>The capabilities assigned to an attendee: audio, video, or content.</p> <note> <p>You use the capabilities with a set of values that control what the capabilities can do, such as <code>SendReceive</code> data. For more information about those values, see .</p> </note> <p>When using capabilities, be aware of these corner cases:</p> <ul> <li> <p>If you specify <code>MeetingFeatures:Video:MaxResolution:None</code> when you create a meeting, all API requests that include <code>SendReceive</code>, <code>Send</code>, or <code>Receive</code> for <code>AttendeeCapabilities:Video</code> will be rejected with <code>ValidationError 400</code>.</p> </li> <li> <p>If you specify <code>MeetingFeatures:Content:MaxResolution:None</code> when you create a meeting, all API requests that include <code>SendReceive</code>, <code>Send</code>, or <code>Receive</code> for <code>AttendeeCapabilities:Content</code> will be rejected with <code>ValidationError 400</code>.</p> </li> <li> <p>You can't set <code>content</code> capabilities to <code>SendReceive</code> or <code>Receive</code> unless you also set <code>video</code> capabilities to <code>SendReceive</code> or <code>Receive</code>. If you don't set the <code>video</code> capability to receive, the response will contain an HTTP 400 Bad Request status code. However, you can set your <code>video</code> capability to receive and you set your <code>content</code> capability to not receive.</p> </li> <li> <p>If meeting features is defined as <code>Video:MaxResolution:None</code> but <code>Content:MaxResolution</code> is defined as something other than <code>None</code> and attendee capabilities are not defined in the API request, then the default attendee video capability is set to <code>Receive</code> and attendee content capability is set to <code>SendReceive</code>. This is because content <code>SendReceive</code> requires video to be at least <code>Receive</code>.</p> </li> <li> <p>When you change an <code>audio</code> capability from <code>None</code> or <code>Receive</code> to <code>Send</code> or <code>SendReceive</code> , and if the attendee left their microphone unmuted, audio will flow from the attendee to the other meeting participants.</p> </li> <li> <p>When you change a <code>video</code> or <code>content</code> capability from <code>None</code> or <code>Receive</code> to <code>Send</code> or <code>SendReceive</code> , and if the attendee turned on their video or content streams, remote attendees can receive those streams, but only after media renegotiation between the client and the Amazon Chime back-end server.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Attendee) -> dict:
    out: dict = {}
    if "external_user_id" in value:
        out["ExternalUserId"] = value["external_user_id"]
    if "attendee_id" in value:
        out["AttendeeId"] = value["attendee_id"]
    if "join_token" in value:
        out["JoinToken"] = value["join_token"]
    if "capabilities" in value:
        import aws_sdk_chime_sdk_meetings.types.attendee_capabilities

        out["Capabilities"] = (
            aws_sdk_chime_sdk_meetings.types.attendee_capabilities.serialize_json(
                value["capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> Attendee:
    out: Attendee = {}  # type: ignore[typeddict-item]
    if "ExternalUserId" in data:
        out["external_user_id"] = data["ExternalUserId"]
    if "AttendeeId" in data:
        out["attendee_id"] = data["AttendeeId"]
    if "JoinToken" in data:
        out["join_token"] = data["JoinToken"]
    if "Capabilities" in data:
        import aws_sdk_chime_sdk_meetings.types.attendee_capabilities

        out["capabilities"] = (
            aws_sdk_chime_sdk_meetings.types.attendee_capabilities.deserialize_json(
                data["Capabilities"]
            )
        )
    return out
