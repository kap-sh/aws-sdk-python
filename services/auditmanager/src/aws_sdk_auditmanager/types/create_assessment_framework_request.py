"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateAssessmentFrameworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.compliance_type
    import aws_sdk_auditmanager.types.create_assessment_framework_control_sets
    import aws_sdk_auditmanager.types.framework_description
    import aws_sdk_auditmanager.types.framework_name
    import aws_sdk_auditmanager.types.tag_map


class CreateAssessmentFrameworkRequest(TypedDict, closed=True):
    name: "aws_sdk_auditmanager.types.framework_name.FrameworkName"
    """<p> The name of the new custom framework. </p>"""
    description: NotRequired[
        "aws_sdk_auditmanager.types.framework_description.FrameworkDescription"
    ]
    """<p> An optional description for the new custom framework. </p>"""
    compliance_type: NotRequired[
        "aws_sdk_auditmanager.types.compliance_type.ComplianceType"
    ]
    """<p> The compliance type that the new custom framework supports, such as CIS or HIPAA. </p>"""
    control_sets: "aws_sdk_auditmanager.types.create_assessment_framework_control_sets.CreateAssessmentFrameworkControlSets"
    """<p> The control sets that are associated with the framework. </p> <note> <p>The <code>Controls</code> object returns a partial response when called through Framework APIs. For a complete <code>Controls</code> object, use <code>GetControl</code>.</p> </note>"""
    tags: NotRequired["aws_sdk_auditmanager.types.tag_map.TagMap"]
    """<p> The tags that are associated with the framework. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssessmentFrameworkRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "compliance_type" in value:
        out["complianceType"] = value["compliance_type"]
    import aws_sdk_auditmanager.types.create_assessment_framework_control_sets

    out["controlSets"] = (
        aws_sdk_auditmanager.types.create_assessment_framework_control_sets.serialize_json(
            value["control_sets"]
        )
    )
    if "tags" in value:
        import aws_sdk_auditmanager.types.tag_map

        out["tags"] = aws_sdk_auditmanager.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAssessmentFrameworkRequest:
    out: CreateAssessmentFrameworkRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssessmentFrameworkRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "complianceType" in data:
        out["compliance_type"] = data["complianceType"]
    if "controlSets" in data:
        import aws_sdk_auditmanager.types.create_assessment_framework_control_sets

        out["control_sets"] = (
            aws_sdk_auditmanager.types.create_assessment_framework_control_sets.deserialize_json(
                data["controlSets"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAssessmentFrameworkRequest.control_sets required"
        )
    if "tags" in data:
        import aws_sdk_auditmanager.types.tag_map

        out["tags"] = aws_sdk_auditmanager.types.tag_map.deserialize_json(data["tags"])
    return out
