"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesFindingFieldsUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.field_map
    import capo_securityhub.types.note_update
    import capo_securityhub.types.ratio_scale
    import capo_securityhub.types.related_finding_list
    import capo_securityhub.types.severity_update
    import capo_securityhub.types.type_list
    import capo_securityhub.types.verification_state
    import capo_securityhub.types.workflow_update


class AutomationRulesFindingFieldsUpdate(TypedDict, closed=True):
    note: NotRequired["capo_securityhub.types.note_update.NoteUpdate"]
    severity: NotRequired["capo_securityhub.types.severity_update.SeverityUpdate"]
    verification_state: NotRequired[
        "capo_securityhub.types.verification_state.VerificationState"
    ]
    """<p> The rule action updates the <code>VerificationState</code> field of a finding. </p>"""
    confidence: NotRequired["capo_securityhub.types.ratio_scale.RatioScale"]
    """<p> The rule action updates the <code>Confidence</code> field of a finding. </p>"""
    criticality: NotRequired["capo_securityhub.types.ratio_scale.RatioScale"]
    """<p> The rule action updates the <code>Criticality</code> field of a finding. </p>"""
    types: NotRequired["capo_securityhub.types.type_list.TypeList"]
    """<p> The rule action updates the <code>Types</code> field of a finding. </p>"""
    user_defined_fields: NotRequired["capo_securityhub.types.field_map.FieldMap"]
    """<p> The rule action updates the <code>UserDefinedFields</code> field of a finding. </p>"""
    workflow: NotRequired["capo_securityhub.types.workflow_update.WorkflowUpdate"]
    related_findings: NotRequired[
        "capo_securityhub.types.related_finding_list.RelatedFindingList"
    ]
    """<p> The rule action updates the <code>RelatedFindings</code> field of a finding. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesFindingFieldsUpdate) -> dict:
    out: dict = {}
    if "note" in value:
        import capo_securityhub.types.note_update

        out["Note"] = capo_securityhub.types.note_update.serialize_json(value["note"])
    if "severity" in value:
        import capo_securityhub.types.severity_update

        out["Severity"] = capo_securityhub.types.severity_update.serialize_json(
            value["severity"]
        )
    if "verification_state" in value:
        import capo_securityhub.types.verification_state

        out["VerificationState"] = (
            capo_securityhub.types.verification_state.serialize_json(
                value["verification_state"]
            )
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "criticality" in value:
        out["Criticality"] = value["criticality"]
    if "types" in value:
        import capo_securityhub.types.type_list

        out["Types"] = capo_securityhub.types.type_list.serialize_json(value["types"])
    if "user_defined_fields" in value:
        import capo_securityhub.types.field_map

        out["UserDefinedFields"] = capo_securityhub.types.field_map.serialize_json(
            value["user_defined_fields"]
        )
    if "workflow" in value:
        import capo_securityhub.types.workflow_update

        out["Workflow"] = capo_securityhub.types.workflow_update.serialize_json(
            value["workflow"]
        )
    if "related_findings" in value:
        import capo_securityhub.types.related_finding_list

        out["RelatedFindings"] = (
            capo_securityhub.types.related_finding_list.serialize_json(
                value["related_findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomationRulesFindingFieldsUpdate:
    out: AutomationRulesFindingFieldsUpdate = {}  # type: ignore[typeddict-item]
    if "Note" in data:
        import capo_securityhub.types.note_update

        out["note"] = capo_securityhub.types.note_update.deserialize_json(data["Note"])
    if "Severity" in data:
        import capo_securityhub.types.severity_update

        out["severity"] = capo_securityhub.types.severity_update.deserialize_json(
            data["Severity"]
        )
    if "VerificationState" in data:
        import capo_securityhub.types.verification_state

        out["verification_state"] = (
            capo_securityhub.types.verification_state.deserialize_json(
                data["VerificationState"]
            )
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Criticality" in data:
        out["criticality"] = data["Criticality"]
    if "Types" in data:
        import capo_securityhub.types.type_list

        out["types"] = capo_securityhub.types.type_list.deserialize_json(data["Types"])
    if "UserDefinedFields" in data:
        import capo_securityhub.types.field_map

        out["user_defined_fields"] = capo_securityhub.types.field_map.deserialize_json(
            data["UserDefinedFields"]
        )
    if "Workflow" in data:
        import capo_securityhub.types.workflow_update

        out["workflow"] = capo_securityhub.types.workflow_update.deserialize_json(
            data["Workflow"]
        )
    if "RelatedFindings" in data:
        import capo_securityhub.types.related_finding_list

        out["related_findings"] = (
            capo_securityhub.types.related_finding_list.deserialize_json(
                data["RelatedFindings"]
            )
        )
    return out
