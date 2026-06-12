"""Generated from Smithy shape ``com.amazonaws.auditmanager#DelegationMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_name
    import aws_sdk_auditmanager.types.delegation_status
    import aws_sdk_auditmanager.types.iam_arn
    import aws_sdk_auditmanager.types.non_empty_string
    import aws_sdk_auditmanager.types.timestamp
    import aws_sdk_auditmanager.types.uuid


class DelegationMetadata(TypedDict):
    id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the delegation. </p>"""
    assessment_name: NotRequired[
        "aws_sdk_auditmanager.types.assessment_name.AssessmentName"
    ]
    """<p> The name of the associated assessment. </p>"""
    assessment_id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the assessment. </p>"""
    status: NotRequired["aws_sdk_auditmanager.types.delegation_status.DelegationStatus"]
    """<p> The current status of the delegation. </p>"""
    role_arn: NotRequired["aws_sdk_auditmanager.types.iam_arn.IamArn"]
    """<p> The Amazon Resource Name (ARN) of the IAM role. </p>"""
    creation_time: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p> Specifies when the delegation was created. </p>"""
    control_set_name: NotRequired[
        "aws_sdk_auditmanager.types.non_empty_string.NonEmptyString"
    ]
    """<p> Specifies the name of the control set that was delegated for review. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DelegationMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "assessment_name" in value:
        out["assessmentName"] = value["assessment_name"]
    if "assessment_id" in value:
        out["assessmentId"] = value["assessment_id"]
    if "status" in value:
        import aws_sdk_auditmanager.types.delegation_status

        out["status"] = aws_sdk_auditmanager.types.delegation_status.serialize_json(
            value["status"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "creation_time" in value:
        import aws_sdk_auditmanager.types.timestamp

        out["creationTime"] = aws_sdk_auditmanager.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "control_set_name" in value:
        out["controlSetName"] = value["control_set_name"]
    return out


def deserialize_json(data: dict) -> DelegationMetadata:
    out: DelegationMetadata = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "assessmentName" in data:
        out["assessment_name"] = data["assessmentName"]
    if "assessmentId" in data:
        out["assessment_id"] = data["assessmentId"]
    if "status" in data:
        import aws_sdk_auditmanager.types.delegation_status

        out["status"] = aws_sdk_auditmanager.types.delegation_status.deserialize_json(
            data["status"]
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "creationTime" in data:
        import aws_sdk_auditmanager.types.timestamp

        out["creation_time"] = aws_sdk_auditmanager.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "controlSetName" in data:
        out["control_set_name"] = data["controlSetName"]
    return out
