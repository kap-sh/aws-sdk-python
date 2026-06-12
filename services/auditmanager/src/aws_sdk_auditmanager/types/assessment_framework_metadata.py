"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentFrameworkMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.audit_manager_arn
    import aws_sdk_auditmanager.types.compliance_type
    import aws_sdk_auditmanager.types.control_sets_count
    import aws_sdk_auditmanager.types.controls_count
    import aws_sdk_auditmanager.types.filename
    import aws_sdk_auditmanager.types.framework_description
    import aws_sdk_auditmanager.types.framework_name
    import aws_sdk_auditmanager.types.framework_type
    import aws_sdk_auditmanager.types.timestamp
    import aws_sdk_auditmanager.types.uuid


class AssessmentFrameworkMetadata(TypedDict):
    arn: NotRequired["aws_sdk_auditmanager.types.audit_manager_arn.AuditManagerArn"]
    """<p> The Amazon Resource Name (ARN) of the framework. </p>"""
    id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the framework. </p>"""
    type: NotRequired["aws_sdk_auditmanager.types.framework_type.FrameworkType"]
    """<p> The framework type, such as a standard framework or a custom framework. </p>"""
    name: NotRequired["aws_sdk_auditmanager.types.framework_name.FrameworkName"]
    """<p> The name of the framework. </p>"""
    description: NotRequired[
        "aws_sdk_auditmanager.types.framework_description.FrameworkDescription"
    ]
    """<p> The description of the framework. </p>"""
    logo: NotRequired["aws_sdk_auditmanager.types.filename.Filename"]
    """<p> The logo that's associated with the framework. </p>"""
    compliance_type: NotRequired[
        "aws_sdk_auditmanager.types.compliance_type.ComplianceType"
    ]
    """<p> The compliance type that the new custom framework supports, such as CIS or HIPAA. </p>"""
    controls_count: "aws_sdk_auditmanager.types.controls_count.ControlsCount"
    """<p> The number of controls that are associated with the framework. </p>"""
    control_sets_count: "aws_sdk_auditmanager.types.control_sets_count.ControlSetsCount"
    """<p> The number of control sets that are associated with the framework. </p>"""
    created_at: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the framework was created. </p>"""
    last_updated_at: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the framework was most recently updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentFrameworkMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import aws_sdk_auditmanager.types.framework_type

        out["type"] = aws_sdk_auditmanager.types.framework_type.serialize_json(
            value["type"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "logo" in value:
        out["logo"] = value["logo"]
    if "compliance_type" in value:
        out["complianceType"] = value["compliance_type"]
    out["controlsCount"] = value.get("controls_count", 0)
    out["controlSetsCount"] = value.get("control_sets_count", 0)
    if "created_at" in value:
        import aws_sdk_auditmanager.types.timestamp

        out["createdAt"] = aws_sdk_auditmanager.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_auditmanager.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_auditmanager.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> AssessmentFrameworkMetadata:
    out: AssessmentFrameworkMetadata = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "type" in data:
        import aws_sdk_auditmanager.types.framework_type

        out["type"] = aws_sdk_auditmanager.types.framework_type.deserialize_json(
            data["type"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "logo" in data:
        out["logo"] = data["logo"]
    if "complianceType" in data:
        out["compliance_type"] = data["complianceType"]
    if "controlsCount" in data:
        out["controls_count"] = data["controlsCount"]
    else:
        out["controls_count"] = 0
    if "controlSetsCount" in data:
        out["control_sets_count"] = data["controlSetsCount"]
    else:
        out["control_sets_count"] = 0
    if "createdAt" in data:
        import aws_sdk_auditmanager.types.timestamp

        out["created_at"] = aws_sdk_auditmanager.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_auditmanager.types.timestamp

        out["last_updated_at"] = aws_sdk_auditmanager.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
