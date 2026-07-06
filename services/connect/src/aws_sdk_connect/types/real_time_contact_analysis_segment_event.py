"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSegmentEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.display_name
    import aws_sdk_connect.types.participant_id
    import aws_sdk_connect.types.participant_role
    import aws_sdk_connect.types.real_time_contact_analysis_event_type
    import aws_sdk_connect.types.real_time_contact_analysis_id256
    import aws_sdk_connect.types.real_time_contact_analysis_time_data


class RealTimeContactAnalysisSegmentEvent(TypedDict, closed=True):
    id: "aws_sdk_connect.types.real_time_contact_analysis_id256.RealTimeContactAnalysisId256"
    """<p>The identifier of the contact event.</p>"""
    participant_id: NotRequired["aws_sdk_connect.types.participant_id.ParticipantId"]
    """<p>The identifier of the participant.</p>"""
    participant_role: NotRequired[
        "aws_sdk_connect.types.participant_role.ParticipantRole"
    ]
    """<p>The role of the participant. For example, is it a customer, agent, or system.</p>"""
    display_name: NotRequired["aws_sdk_connect.types.display_name.DisplayName"]
    """<p>The display name of the participant. Can be redacted.</p>"""
    event_type: "aws_sdk_connect.types.real_time_contact_analysis_event_type.RealTimeContactAnalysisEventType"
    """<p>Type of the event. For example, <code>application/vnd.amazonaws.connect.event.participant.left</code>.</p>"""
    time: "aws_sdk_connect.types.real_time_contact_analysis_time_data.RealTimeContactAnalysisTimeData"
    """<p>Field describing the time of the event. It can have different representations of time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSegmentEvent) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "participant_id" in value:
        out["ParticipantId"] = value["participant_id"]
    if "participant_role" in value:
        import aws_sdk_connect.types.participant_role

        out["ParticipantRole"] = aws_sdk_connect.types.participant_role.serialize_json(
            value["participant_role"]
        )
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    out["EventType"] = value["event_type"]
    import aws_sdk_connect.types.real_time_contact_analysis_time_data

    out["Time"] = (
        aws_sdk_connect.types.real_time_contact_analysis_time_data.serialize_json(
            value["time"]
        )
    )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisSegmentEvent:
    out: RealTimeContactAnalysisSegmentEvent = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("RealTimeContactAnalysisSegmentEvent.id required")
    if "ParticipantId" in data:
        out["participant_id"] = data["ParticipantId"]
    if "ParticipantRole" in data:
        import aws_sdk_connect.types.participant_role

        out["participant_role"] = (
            aws_sdk_connect.types.participant_role.deserialize_json(
                data["ParticipantRole"]
            )
        )
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "EventType" in data:
        out["event_type"] = data["EventType"]
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentEvent.event_type required"
        )
    if "Time" in data:
        import aws_sdk_connect.types.real_time_contact_analysis_time_data

        out["time"] = (
            aws_sdk_connect.types.real_time_contact_analysis_time_data.deserialize_json(
                data["Time"]
            )
        )
    else:
        raise DeserializationError("RealTimeContactAnalysisSegmentEvent.time required")
    return out
