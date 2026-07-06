"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_security_finding_identifier_list
    import aws_sdk_securityhub.types.field_map
    import aws_sdk_securityhub.types.note_update
    import aws_sdk_securityhub.types.ratio_scale
    import aws_sdk_securityhub.types.related_finding_list
    import aws_sdk_securityhub.types.severity_update
    import aws_sdk_securityhub.types.type_list
    import aws_sdk_securityhub.types.verification_state
    import aws_sdk_securityhub.types.workflow_update


class BatchUpdateFindingsRequest(TypedDict, closed=True):
    finding_identifiers: NotRequired[
        "aws_sdk_securityhub.types.aws_security_finding_identifier_list.AwsSecurityFindingIdentifierList"
    ]
    """<p>The list of findings to update. <code>BatchUpdateFindings</code> can be used to update up to 100 findings at a time.</p> <p>For each finding, the list provides the finding identifier and the ARN of the finding provider.</p>"""
    note: NotRequired["aws_sdk_securityhub.types.note_update.NoteUpdate"]
    severity: NotRequired["aws_sdk_securityhub.types.severity_update.SeverityUpdate"]
    """<p>Used to update the finding severity.</p>"""
    verification_state: NotRequired[
        "aws_sdk_securityhub.types.verification_state.VerificationState"
    ]
    """<p>Indicates the veracity of a finding.</p> <p>The available values for <code>VerificationState</code> are as follows.</p> <ul> <li> <p> <code>UNKNOWN</code> – The default disposition of a security finding</p> </li> <li> <p> <code>TRUE_POSITIVE</code> – The security finding is confirmed</p> </li> <li> <p> <code>FALSE_POSITIVE</code> – The security finding was determined to be a false alarm</p> </li> <li> <p> <code>BENIGN_POSITIVE</code> – A special case of <code>TRUE_POSITIVE</code> where the finding doesn't pose any threat, is expected, or both</p> </li> </ul>"""
    confidence: NotRequired["aws_sdk_securityhub.types.ratio_scale.RatioScale"]
    """<p>The updated value for the finding confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.</p> <p>Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.</p>"""
    criticality: NotRequired["aws_sdk_securityhub.types.ratio_scale.RatioScale"]
    """<p>The updated value for the level of importance assigned to the resources associated with the findings.</p> <p>A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources. </p>"""
    types: NotRequired["aws_sdk_securityhub.types.type_list.TypeList"]
    """<p>One or more finding types in the format of namespace/category/classifier that classify a finding.</p> <p>Valid namespace values are as follows.</p> <ul> <li> <p>Software and Configuration Checks</p> </li> <li> <p>TTPs</p> </li> <li> <p>Effects</p> </li> <li> <p>Unusual Behaviors</p> </li> <li> <p>Sensitive Data Identifications </p> </li> </ul>"""
    user_defined_fields: NotRequired["aws_sdk_securityhub.types.field_map.FieldMap"]
    """<p>A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.</p>"""
    workflow: NotRequired["aws_sdk_securityhub.types.workflow_update.WorkflowUpdate"]
    """<p>Used to update the workflow status of a finding.</p> <p>The workflow status indicates the progress of the investigation into the finding. </p>"""
    related_findings: NotRequired[
        "aws_sdk_securityhub.types.related_finding_list.RelatedFindingList"
    ]
    """<p>A list of findings that are related to the updated findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFindingsRequest) -> dict:
    out: dict = {}
    if "finding_identifiers" in value:
        import aws_sdk_securityhub.types.aws_security_finding_identifier_list

        out["FindingIdentifiers"] = (
            aws_sdk_securityhub.types.aws_security_finding_identifier_list.serialize_json(
                value["finding_identifiers"]
            )
        )
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


def deserialize_json(data: dict) -> BatchUpdateFindingsRequest:
    out: BatchUpdateFindingsRequest = {}  # type: ignore[typeddict-item]
    if "FindingIdentifiers" in data:
        import aws_sdk_securityhub.types.aws_security_finding_identifier_list

        out["finding_identifiers"] = (
            aws_sdk_securityhub.types.aws_security_finding_identifier_list.deserialize_json(
                data["FindingIdentifiers"]
            )
        )
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
