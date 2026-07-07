"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSegmentAttachments``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.display_name
    import aws_sdk_connect.types.participant_id
    import aws_sdk_connect.types.participant_role
    import aws_sdk_connect.types.real_time_contact_analysis_attachments
    import aws_sdk_connect.types.real_time_contact_analysis_id256
    import aws_sdk_connect.types.real_time_contact_analysis_time_data


class RealTimeContactAnalysisSegmentAttachments(TypedDict, closed=True):
    id: "aws_sdk_connect.types.real_time_contact_analysis_id256.RealTimeContactAnalysisId256"
    """<p>The identifier of the segment.</p>"""
    participant_id: "aws_sdk_connect.types.participant_id.ParticipantId"
    """<p>The identifier of the participant.</p>"""
    participant_role: "aws_sdk_connect.types.participant_role.ParticipantRole"
    """<p>The role of the participant. For example, is it a customer, agent, or system.</p>"""
    display_name: NotRequired["aws_sdk_connect.types.display_name.DisplayName"]
    """<p>The display name of the participant. Can be redacted. </p>"""
    attachments: "aws_sdk_connect.types.real_time_contact_analysis_attachments.RealTimeContactAnalysisAttachments"
    """<p>List of objects describing an individual attachment.</p>"""
    time: "aws_sdk_connect.types.real_time_contact_analysis_time_data.RealTimeContactAnalysisTimeData"
    """<p>Field describing the time of the event. It can have different representations of time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSegmentAttachments) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["ParticipantId"] = value["participant_id"]
    import aws_sdk_connect.types.participant_role

    out["ParticipantRole"] = aws_sdk_connect.types.participant_role.serialize_json(
        value["participant_role"]
    )
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    import aws_sdk_connect.types.real_time_contact_analysis_attachments

    out["Attachments"] = (
        aws_sdk_connect.types.real_time_contact_analysis_attachments.serialize_json(
            value["attachments"]
        )
    )
    import aws_sdk_connect.types.real_time_contact_analysis_time_data

    out["Time"] = (
        aws_sdk_connect.types.real_time_contact_analysis_time_data.serialize_json(
            value["time"]
        )
    )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisSegmentAttachments:
    out: RealTimeContactAnalysisSegmentAttachments = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentAttachments.id required"
        )
    if "ParticipantId" in data:
        out["participant_id"] = data["ParticipantId"]
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentAttachments.participant_id required"
        )
    if "ParticipantRole" in data:
        import aws_sdk_connect.types.participant_role

        out["participant_role"] = (
            aws_sdk_connect.types.participant_role.deserialize_json(
                data["ParticipantRole"]
            )
        )
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentAttachments.participant_role required"
        )
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Attachments" in data:
        import aws_sdk_connect.types.real_time_contact_analysis_attachments

        out["attachments"] = (
            aws_sdk_connect.types.real_time_contact_analysis_attachments.deserialize_json(
                data["Attachments"]
            )
        )
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentAttachments.attachments required"
        )
    if "Time" in data:
        import aws_sdk_connect.types.real_time_contact_analysis_time_data

        out["time"] = (
            aws_sdk_connect.types.real_time_contact_analysis_time_data.deserialize_json(
                data["Time"]
            )
        )
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentAttachments.time required"
        )
    return out
