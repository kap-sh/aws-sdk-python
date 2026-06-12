"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentFrameworkRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.compliance_type
    import aws_sdk_auditmanager.types.framework_description
    import aws_sdk_auditmanager.types.framework_name
    import aws_sdk_auditmanager.types.update_assessment_framework_control_sets
    import aws_sdk_auditmanager.types.uuid


class UpdateAssessmentFrameworkRequest(TypedDict):
    framework_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the framework. </p>"""
    name: "aws_sdk_auditmanager.types.framework_name.FrameworkName"
    """<p> The name of the framework to be updated. </p>"""
    description: NotRequired[
        "aws_sdk_auditmanager.types.framework_description.FrameworkDescription"
    ]
    """<p> The description of the updated framework. </p>"""
    compliance_type: NotRequired[
        "aws_sdk_auditmanager.types.compliance_type.ComplianceType"
    ]
    """<p> The compliance type that the new custom framework supports, such as CIS or HIPAA. </p>"""
    control_sets: "aws_sdk_auditmanager.types.update_assessment_framework_control_sets.UpdateAssessmentFrameworkControlSets"
    """<p> The control sets that are associated with the framework. </p> <note> <p>The <code>Controls</code> object returns a partial response when called through Framework APIs. For a complete <code>Controls</code> object, use <code>GetControl</code>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentFrameworkRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "compliance_type" in value:
        out["complianceType"] = value["compliance_type"]
    import aws_sdk_auditmanager.types.update_assessment_framework_control_sets

    out["controlSets"] = (
        aws_sdk_auditmanager.types.update_assessment_framework_control_sets.serialize_json(
            value["control_sets"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentFrameworkRequest:
    out: UpdateAssessmentFrameworkRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateAssessmentFrameworkRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "complianceType" in data:
        out["compliance_type"] = data["complianceType"]
    if "controlSets" in data:
        import aws_sdk_auditmanager.types.update_assessment_framework_control_sets

        out["control_sets"] = (
            aws_sdk_auditmanager.types.update_assessment_framework_control_sets.deserialize_json(
                data["controlSets"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAssessmentFrameworkRequest.control_sets required"
        )
    return out
