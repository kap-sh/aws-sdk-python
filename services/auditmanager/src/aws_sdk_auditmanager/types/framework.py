"""Generated from Smithy shape ``com.amazonaws.auditmanager#Framework``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.audit_manager_arn
    import aws_sdk_auditmanager.types.compliance_type
    import aws_sdk_auditmanager.types.control_sets
    import aws_sdk_auditmanager.types.control_sources
    import aws_sdk_auditmanager.types.created_by
    import aws_sdk_auditmanager.types.filename
    import aws_sdk_auditmanager.types.framework_description
    import aws_sdk_auditmanager.types.framework_name
    import aws_sdk_auditmanager.types.framework_type
    import aws_sdk_auditmanager.types.last_updated_by
    import aws_sdk_auditmanager.types.tag_map
    import aws_sdk_auditmanager.types.timestamp
    import aws_sdk_auditmanager.types.uuid


class Framework(TypedDict):
    arn: NotRequired["aws_sdk_auditmanager.types.audit_manager_arn.AuditManagerArn"]
    """<p> The Amazon Resource Name (ARN) of the framework. </p>"""
    id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the framework. </p>"""
    name: NotRequired["aws_sdk_auditmanager.types.framework_name.FrameworkName"]
    """<p> The name of the framework. </p>"""
    type: NotRequired["aws_sdk_auditmanager.types.framework_type.FrameworkType"]
    """<p> Specifies whether the framework is a standard framework or a custom framework.</p>"""
    compliance_type: NotRequired[
        "aws_sdk_auditmanager.types.compliance_type.ComplianceType"
    ]
    """<p> The compliance type that the framework supports, such as CIS or HIPAA. </p>"""
    description: NotRequired[
        "aws_sdk_auditmanager.types.framework_description.FrameworkDescription"
    ]
    """<p> The description of the framework. </p>"""
    logo: NotRequired["aws_sdk_auditmanager.types.filename.Filename"]
    """<p> The logo that's associated with the framework. </p>"""
    control_sources: NotRequired[
        "aws_sdk_auditmanager.types.control_sources.ControlSources"
    ]
    """<p> The control data sources where Audit Manager collects evidence from.</p> <important> <p>This API parameter is no longer supported.</p> </important>"""
    control_sets: NotRequired["aws_sdk_auditmanager.types.control_sets.ControlSets"]
    """<p> The control sets that are associated with the framework. </p> <note> <p>The <code>Controls</code> object returns a partial response when called through Framework APIs. For a complete <code>Controls</code> object, use <code>GetControl</code>.</p> </note>"""
    created_at: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the framework was created. </p>"""
    last_updated_at: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the framework was most recently updated. </p>"""
    created_by: NotRequired["aws_sdk_auditmanager.types.created_by.CreatedBy"]
    """<p> The user or role that created the framework. </p>"""
    last_updated_by: NotRequired[
        "aws_sdk_auditmanager.types.last_updated_by.LastUpdatedBy"
    ]
    """<p> The user or role that most recently updated the framework. </p>"""
    tags: NotRequired["aws_sdk_auditmanager.types.tag_map.TagMap"]
    """<p> The tags that are associated with the framework. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Framework) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import aws_sdk_auditmanager.types.framework_type

        out["type"] = aws_sdk_auditmanager.types.framework_type.serialize_json(
            value["type"]
        )
    if "compliance_type" in value:
        out["complianceType"] = value["compliance_type"]
    if "description" in value:
        out["description"] = value["description"]
    if "logo" in value:
        out["logo"] = value["logo"]
    if "control_sources" in value:
        out["controlSources"] = value["control_sources"]
    if "control_sets" in value:
        import aws_sdk_auditmanager.types.control_sets

        out["controlSets"] = aws_sdk_auditmanager.types.control_sets.serialize_json(
            value["control_sets"]
        )
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
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    if "tags" in value:
        import aws_sdk_auditmanager.types.tag_map

        out["tags"] = aws_sdk_auditmanager.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Framework:
    out: Framework = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import aws_sdk_auditmanager.types.framework_type

        out["type"] = aws_sdk_auditmanager.types.framework_type.deserialize_json(
            data["type"]
        )
    if "complianceType" in data:
        out["compliance_type"] = data["complianceType"]
    if "description" in data:
        out["description"] = data["description"]
    if "logo" in data:
        out["logo"] = data["logo"]
    if "controlSources" in data:
        out["control_sources"] = data["controlSources"]
    if "controlSets" in data:
        import aws_sdk_auditmanager.types.control_sets

        out["control_sets"] = aws_sdk_auditmanager.types.control_sets.deserialize_json(
            data["controlSets"]
        )
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
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "lastUpdatedBy" in data:
        out["last_updated_by"] = data["lastUpdatedBy"]
    if "tags" in data:
        import aws_sdk_auditmanager.types.tag_map

        out["tags"] = aws_sdk_auditmanager.types.tag_map.deserialize_json(data["tags"])
    return out
