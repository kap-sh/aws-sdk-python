"""Generated from Smithy shape ``com.amazonaws.auditmanager#Notification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_name
    import capo_auditmanager.types.control_set_id
    import capo_auditmanager.types.non_empty_string
    import capo_auditmanager.types.timestamp
    import capo_auditmanager.types.timestamp_uuid
    import capo_auditmanager.types.uuid


class Notification(TypedDict, closed=True):
    id: NotRequired["capo_auditmanager.types.timestamp_uuid.TimestampUUID"]
    """<p> The unique identifier for the notification. </p>"""
    assessment_id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The identifier for the assessment. </p>"""
    assessment_name: NotRequired[
        "capo_auditmanager.types.assessment_name.AssessmentName"
    ]
    """<p> The name of the related assessment. </p>"""
    control_set_id: NotRequired["capo_auditmanager.types.control_set_id.ControlSetId"]
    """<p> The identifier for the control set. </p>"""
    control_set_name: NotRequired[
        "capo_auditmanager.types.non_empty_string.NonEmptyString"
    ]
    """<p> Specifies the name of the control set that the notification is about. </p>"""
    description: NotRequired["capo_auditmanager.types.non_empty_string.NonEmptyString"]
    """<p> The description of the notification. </p>"""
    event_time: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the notification was sent. </p>"""
    source: NotRequired["capo_auditmanager.types.non_empty_string.NonEmptyString"]
    """<p> The sender of the notification. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Notification) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "assessment_id" in value:
        out["assessmentId"] = value["assessment_id"]
    if "assessment_name" in value:
        out["assessmentName"] = value["assessment_name"]
    if "control_set_id" in value:
        out["controlSetId"] = value["control_set_id"]
    if "control_set_name" in value:
        out["controlSetName"] = value["control_set_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "event_time" in value:
        import capo_auditmanager.types.timestamp

        out["eventTime"] = capo_auditmanager.types.timestamp.serialize_json(
            value["event_time"]
        )
    if "source" in value:
        out["source"] = value["source"]
    return out


def deserialize_json(data: dict) -> Notification:
    out: Notification = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "assessmentId" in data:
        out["assessment_id"] = data["assessmentId"]
    if "assessmentName" in data:
        out["assessment_name"] = data["assessmentName"]
    if "controlSetId" in data:
        out["control_set_id"] = data["controlSetId"]
    if "controlSetName" in data:
        out["control_set_name"] = data["controlSetName"]
    if "description" in data:
        out["description"] = data["description"]
    if "eventTime" in data:
        import capo_auditmanager.types.timestamp

        out["event_time"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["eventTime"]
        )
    if "source" in data:
        out["source"] = data["source"]
    return out
