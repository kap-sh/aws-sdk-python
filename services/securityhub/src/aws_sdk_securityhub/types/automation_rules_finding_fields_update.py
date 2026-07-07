"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesFindingFieldsUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.field_map
    import aws_sdk_securityhub.types.note_update
    import aws_sdk_securityhub.types.ratio_scale
    import aws_sdk_securityhub.types.related_finding_list
    import aws_sdk_securityhub.types.severity_update
    import aws_sdk_securityhub.types.type_list
    import aws_sdk_securityhub.types.verification_state
    import aws_sdk_securityhub.types.workflow_update


class AutomationRulesFindingFieldsUpdate(TypedDict, closed=True):
    note: NotRequired["aws_sdk_securityhub.types.note_update.NoteUpdate"]
    severity: NotRequired["aws_sdk_securityhub.types.severity_update.SeverityUpdate"]
    verification_state: NotRequired[
        "aws_sdk_securityhub.types.verification_state.VerificationState"
    ]
    """<p> The rule action updates the <code>VerificationState</code> field of a finding. </p>"""
    confidence: NotRequired["aws_sdk_securityhub.types.ratio_scale.RatioScale"]
    """<p> The rule action updates the <code>Confidence</code> field of a finding. </p>"""
    criticality: NotRequired["aws_sdk_securityhub.types.ratio_scale.RatioScale"]
    """<p> The rule action updates the <code>Criticality</code> field of a finding. </p>"""
    types: NotRequired["aws_sdk_securityhub.types.type_list.TypeList"]
    """<p> The rule action updates the <code>Types</code> field of a finding. </p>"""
    user_defined_fields: NotRequired["aws_sdk_securityhub.types.field_map.FieldMap"]
    """<p> The rule action updates the <code>UserDefinedFields</code> field of a finding. </p>"""
    workflow: NotRequired["aws_sdk_securityhub.types.workflow_update.WorkflowUpdate"]
    related_findings: NotRequired[
        "aws_sdk_securityhub.types.related_finding_list.RelatedFindingList"
    ]
    """<p> The rule action updates the <code>RelatedFindings</code> field of a finding. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesFindingFieldsUpdate) -> dict:
    out: dict = {}
    if "note" in value:
        import aws_sdk_securityhub.types.note_update

        out["Note"] = aws_sdk_securityhub.types.note_update.serialize_json(
            value["note"]
        )
    if "severity" in value:
        import aws_sdk_securityhub.types.severity_update

        out["Severity"] = aws_sdk_securityhub.types.severity_update.serialize_json(
            value["severity"]
        )
    if "verification_state" in value:
        import aws_sdk_securityhub.types.verification_state

        out["VerificationState"] = (
            aws_sdk_securityhub.types.verification_state.serialize_json(
                value["verification_state"]
            )
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "criticality" in value:
        out["Criticality"] = value["criticality"]
    if "types" in value:
        import aws_sdk_securityhub.types.type_list

        out["Types"] = aws_sdk_securityhub.types.type_list.serialize_json(
            value["types"]
        )
    if "user_defined_fields" in value:
        import aws_sdk_securityhub.types.field_map

        out["UserDefinedFields"] = aws_sdk_securityhub.types.field_map.serialize_json(
            value["user_defined_fields"]
        )
    if "workflow" in value:
        import aws_sdk_securityhub.types.workflow_update

        out["Workflow"] = aws_sdk_securityhub.types.workflow_update.serialize_json(
            value["workflow"]
        )
    if "related_findings" in value:
        import aws_sdk_securityhub.types.related_finding_list

        out["RelatedFindings"] = (
            aws_sdk_securityhub.types.related_finding_list.serialize_json(
                value["related_findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomationRulesFindingFieldsUpdate:
    out: AutomationRulesFindingFieldsUpdate = {}  # type: ignore[typeddict-item]
    if "Note" in data:
        import aws_sdk_securityhub.types.note_update

        out["note"] = aws_sdk_securityhub.types.note_update.deserialize_json(
            data["Note"]
        )
    if "Severity" in data:
        import aws_sdk_securityhub.types.severity_update

        out["severity"] = aws_sdk_securityhub.types.severity_update.deserialize_json(
            data["Severity"]
        )
    if "VerificationState" in data:
        import aws_sdk_securityhub.types.verification_state

        out["verification_state"] = (
            aws_sdk_securityhub.types.verification_state.deserialize_json(
                data["VerificationState"]
            )
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Criticality" in data:
        out["criticality"] = data["Criticality"]
    if "Types" in data:
        import aws_sdk_securityhub.types.type_list

        out["types"] = aws_sdk_securityhub.types.type_list.deserialize_json(
            data["Types"]
        )
    if "UserDefinedFields" in data:
        import aws_sdk_securityhub.types.field_map

        out["user_defined_fields"] = (
            aws_sdk_securityhub.types.field_map.deserialize_json(
                data["UserDefinedFields"]
            )
        )
    if "Workflow" in data:
        import aws_sdk_securityhub.types.workflow_update

        out["workflow"] = aws_sdk_securityhub.types.workflow_update.deserialize_json(
            data["Workflow"]
        )
    if "RelatedFindings" in data:
        import aws_sdk_securityhub.types.related_finding_list

        out["related_findings"] = (
            aws_sdk_securityhub.types.related_finding_list.deserialize_json(
                data["RelatedFindings"]
            )
        )
    return out
