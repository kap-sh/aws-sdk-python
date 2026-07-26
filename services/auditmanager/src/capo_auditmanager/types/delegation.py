"""Generated from Smithy shape ``com.amazonaws.auditmanager#Delegation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_name
    import capo_auditmanager.types.control_set_id
    import capo_auditmanager.types.created_by
    import capo_auditmanager.types.delegation_comment
    import capo_auditmanager.types.delegation_status
    import capo_auditmanager.types.iam_arn
    import capo_auditmanager.types.role_type
    import capo_auditmanager.types.timestamp
    import capo_auditmanager.types.uuid


class Delegation(TypedDict, closed=True):
    id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the delegation. </p>"""
    assessment_name: NotRequired[
        "capo_auditmanager.types.assessment_name.AssessmentName"
    ]
    """<p> The name of the assessment that's associated with the delegation. </p>"""
    assessment_id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The identifier for the assessment that's associated with the delegation. </p>"""
    status: NotRequired["capo_auditmanager.types.delegation_status.DelegationStatus"]
    """<p> The status of the delegation. </p>"""
    role_arn: NotRequired["capo_auditmanager.types.iam_arn.IamArn"]
    """<p> The Amazon Resource Name (ARN) of the IAM role. </p>"""
    role_type: NotRequired["capo_auditmanager.types.role_type.RoleType"]
    """<p> The type of customer persona. </p> <note> <p>In <code>CreateAssessment</code>, <code>roleType</code> can only be <code>PROCESS_OWNER</code>. </p> <p>In <code>UpdateSettings</code>, <code>roleType</code> can only be <code>PROCESS_OWNER</code>.</p> <p>In <code>BatchCreateDelegationByAssessment</code>, <code>roleType</code> can only be <code>RESOURCE_OWNER</code>.</p> </note>"""
    creation_time: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> Specifies when the delegation was created. </p>"""
    last_updated: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> Specifies when the delegation was last updated. </p>"""
    control_set_id: NotRequired["capo_auditmanager.types.control_set_id.ControlSetId"]
    """<p> The identifier for the control set that's associated with the delegation. </p>"""
    comment: NotRequired["capo_auditmanager.types.delegation_comment.DelegationComment"]
    """<p> The comment that's related to the delegation. </p>"""
    created_by: NotRequired["capo_auditmanager.types.created_by.CreatedBy"]
    """<p> The user or role that created the delegation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Delegation) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "assessment_name" in value:
        out["assessmentName"] = value["assessment_name"]
    if "assessment_id" in value:
        out["assessmentId"] = value["assessment_id"]
    if "status" in value:
        import capo_auditmanager.types.delegation_status

        out["status"] = capo_auditmanager.types.delegation_status.serialize_json(
            value["status"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "role_type" in value:
        import capo_auditmanager.types.role_type

        out["roleType"] = capo_auditmanager.types.role_type.serialize_json(
            value["role_type"]
        )
    if "creation_time" in value:
        import capo_auditmanager.types.timestamp

        out["creationTime"] = capo_auditmanager.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated" in value:
        import capo_auditmanager.types.timestamp

        out["lastUpdated"] = capo_auditmanager.types.timestamp.serialize_json(
            value["last_updated"]
        )
    if "control_set_id" in value:
        out["controlSetId"] = value["control_set_id"]
    if "comment" in value:
        out["comment"] = value["comment"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> Delegation:
    out: Delegation = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "assessmentName" in data:
        out["assessment_name"] = data["assessmentName"]
    if "assessmentId" in data:
        out["assessment_id"] = data["assessmentId"]
    if "status" in data:
        import capo_auditmanager.types.delegation_status

        out["status"] = capo_auditmanager.types.delegation_status.deserialize_json(
            data["status"]
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "roleType" in data:
        import capo_auditmanager.types.role_type

        out["role_type"] = capo_auditmanager.types.role_type.deserialize_json(
            data["roleType"]
        )
    if "creationTime" in data:
        import capo_auditmanager.types.timestamp

        out["creation_time"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdated" in data:
        import capo_auditmanager.types.timestamp

        out["last_updated"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["lastUpdated"]
        )
    if "controlSetId" in data:
        out["control_set_id"] = data["controlSetId"]
    if "comment" in data:
        out["comment"] = data["comment"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    return out
