"""Generated from Smithy shape ``com.amazonaws.iot#AuditFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.audit_check_name
    import capo_iot.types.audit_finding_severity
    import capo_iot.types.audit_task_id
    import capo_iot.types.finding_id
    import capo_iot.types.is_suppressed
    import capo_iot.types.non_compliant_resource
    import capo_iot.types.reason_for_non_compliance
    import capo_iot.types.reason_for_non_compliance_code
    import capo_iot.types.related_resources
    import capo_iot.types.timestamp


class AuditFinding(TypedDict, closed=True):
    finding_id: NotRequired["capo_iot.types.finding_id.FindingId"]
    """<p>A unique identifier for this set of audit findings. This identifier is used to apply mitigation tasks to one or more sets of findings.</p>"""
    task_id: NotRequired["capo_iot.types.audit_task_id.AuditTaskId"]
    """<p>The ID of the audit that generated this result (finding).</p>"""
    check_name: NotRequired["capo_iot.types.audit_check_name.AuditCheckName"]
    """<p>The audit check that generated this result.</p>"""
    task_start_time: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p>The time the audit started.</p>"""
    finding_time: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p>The time the result (finding) was discovered.</p>"""
    severity: NotRequired["capo_iot.types.audit_finding_severity.AuditFindingSeverity"]
    """<p>The severity of the result (finding).</p>"""
    non_compliant_resource: NotRequired[
        "capo_iot.types.non_compliant_resource.NonCompliantResource"
    ]
    """<p>The resource that was found to be noncompliant with the audit check.</p>"""
    related_resources: NotRequired["capo_iot.types.related_resources.RelatedResources"]
    """<p>The list of related resources.</p>"""
    reason_for_non_compliance: NotRequired[
        "capo_iot.types.reason_for_non_compliance.ReasonForNonCompliance"
    ]
    """<p>The reason the resource was noncompliant.</p>"""
    reason_for_non_compliance_code: NotRequired[
        "capo_iot.types.reason_for_non_compliance_code.ReasonForNonComplianceCode"
    ]
    """<p>A code that indicates the reason that the resource was noncompliant.</p>"""
    is_suppressed: NotRequired["capo_iot.types.is_suppressed.IsSuppressed"]
    """<p> Indicates whether the audit finding was suppressed or not during reporting. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditFinding) -> dict:
    out: dict = {}
    if "finding_id" in value:
        out["findingId"] = value["finding_id"]
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "check_name" in value:
        out["checkName"] = value["check_name"]
    if "task_start_time" in value:
        import capo_iot.types.timestamp

        out["taskStartTime"] = capo_iot.types.timestamp.serialize_json(
            value["task_start_time"]
        )
    if "finding_time" in value:
        import capo_iot.types.timestamp

        out["findingTime"] = capo_iot.types.timestamp.serialize_json(
            value["finding_time"]
        )
    if "severity" in value:
        import capo_iot.types.audit_finding_severity

        out["severity"] = capo_iot.types.audit_finding_severity.serialize_json(
            value["severity"]
        )
    if "non_compliant_resource" in value:
        import capo_iot.types.non_compliant_resource

        out["nonCompliantResource"] = (
            capo_iot.types.non_compliant_resource.serialize_json(
                value["non_compliant_resource"]
            )
        )
    if "related_resources" in value:
        import capo_iot.types.related_resources

        out["relatedResources"] = capo_iot.types.related_resources.serialize_json(
            value["related_resources"]
        )
    if "reason_for_non_compliance" in value:
        out["reasonForNonCompliance"] = value["reason_for_non_compliance"]
    if "reason_for_non_compliance_code" in value:
        out["reasonForNonComplianceCode"] = value["reason_for_non_compliance_code"]
    if "is_suppressed" in value:
        out["isSuppressed"] = value["is_suppressed"]
    return out


def deserialize_json(data: dict) -> AuditFinding:
    out: AuditFinding = {}  # type: ignore[typeddict-item]
    if "findingId" in data:
        out["finding_id"] = data["findingId"]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "checkName" in data:
        out["check_name"] = data["checkName"]
    if "taskStartTime" in data:
        import capo_iot.types.timestamp

        out["task_start_time"] = capo_iot.types.timestamp.deserialize_json(
            data["taskStartTime"]
        )
    if "findingTime" in data:
        import capo_iot.types.timestamp

        out["finding_time"] = capo_iot.types.timestamp.deserialize_json(
            data["findingTime"]
        )
    if "severity" in data:
        import capo_iot.types.audit_finding_severity

        out["severity"] = capo_iot.types.audit_finding_severity.deserialize_json(
            data["severity"]
        )
    if "nonCompliantResource" in data:
        import capo_iot.types.non_compliant_resource

        out["non_compliant_resource"] = (
            capo_iot.types.non_compliant_resource.deserialize_json(
                data["nonCompliantResource"]
            )
        )
    if "relatedResources" in data:
        import capo_iot.types.related_resources

        out["related_resources"] = capo_iot.types.related_resources.deserialize_json(
            data["relatedResources"]
        )
    if "reasonForNonCompliance" in data:
        out["reason_for_non_compliance"] = data["reasonForNonCompliance"]
    if "reasonForNonComplianceCode" in data:
        out["reason_for_non_compliance_code"] = data["reasonForNonComplianceCode"]
    if "isSuppressed" in data:
        out["is_suppressed"] = data["isSuppressed"]
    return out
