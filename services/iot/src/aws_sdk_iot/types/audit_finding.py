"""Generated from Smithy shape ``com.amazonaws.iot#AuditFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_check_name
    import aws_sdk_iot.types.audit_finding_severity
    import aws_sdk_iot.types.audit_task_id
    import aws_sdk_iot.types.finding_id
    import aws_sdk_iot.types.is_suppressed
    import aws_sdk_iot.types.non_compliant_resource
    import aws_sdk_iot.types.reason_for_non_compliance
    import aws_sdk_iot.types.reason_for_non_compliance_code
    import aws_sdk_iot.types.related_resources
    import aws_sdk_iot.types.timestamp


class AuditFinding(TypedDict, closed=True):
    finding_id: NotRequired["aws_sdk_iot.types.finding_id.FindingId"]
    """<p>A unique identifier for this set of audit findings. This identifier is used to apply mitigation tasks to one or more sets of findings.</p>"""
    task_id: NotRequired["aws_sdk_iot.types.audit_task_id.AuditTaskId"]
    """<p>The ID of the audit that generated this result (finding).</p>"""
    check_name: NotRequired["aws_sdk_iot.types.audit_check_name.AuditCheckName"]
    """<p>The audit check that generated this result.</p>"""
    task_start_time: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p>The time the audit started.</p>"""
    finding_time: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p>The time the result (finding) was discovered.</p>"""
    severity: NotRequired[
        "aws_sdk_iot.types.audit_finding_severity.AuditFindingSeverity"
    ]
    """<p>The severity of the result (finding).</p>"""
    non_compliant_resource: NotRequired[
        "aws_sdk_iot.types.non_compliant_resource.NonCompliantResource"
    ]
    """<p>The resource that was found to be noncompliant with the audit check.</p>"""
    related_resources: NotRequired[
        "aws_sdk_iot.types.related_resources.RelatedResources"
    ]
    """<p>The list of related resources.</p>"""
    reason_for_non_compliance: NotRequired[
        "aws_sdk_iot.types.reason_for_non_compliance.ReasonForNonCompliance"
    ]
    """<p>The reason the resource was noncompliant.</p>"""
    reason_for_non_compliance_code: NotRequired[
        "aws_sdk_iot.types.reason_for_non_compliance_code.ReasonForNonComplianceCode"
    ]
    """<p>A code that indicates the reason that the resource was noncompliant.</p>"""
    is_suppressed: NotRequired["aws_sdk_iot.types.is_suppressed.IsSuppressed"]
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
        import aws_sdk_iot.types.timestamp

        out["taskStartTime"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["task_start_time"]
        )
    if "finding_time" in value:
        import aws_sdk_iot.types.timestamp

        out["findingTime"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["finding_time"]
        )
    if "severity" in value:
        import aws_sdk_iot.types.audit_finding_severity

        out["severity"] = aws_sdk_iot.types.audit_finding_severity.serialize_json(
            value["severity"]
        )
    if "non_compliant_resource" in value:
        import aws_sdk_iot.types.non_compliant_resource

        out["nonCompliantResource"] = (
            aws_sdk_iot.types.non_compliant_resource.serialize_json(
                value["non_compliant_resource"]
            )
        )
    if "related_resources" in value:
        import aws_sdk_iot.types.related_resources

        out["relatedResources"] = aws_sdk_iot.types.related_resources.serialize_json(
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
        import aws_sdk_iot.types.timestamp

        out["task_start_time"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["taskStartTime"]
        )
    if "findingTime" in data:
        import aws_sdk_iot.types.timestamp

        out["finding_time"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["findingTime"]
        )
    if "severity" in data:
        import aws_sdk_iot.types.audit_finding_severity

        out["severity"] = aws_sdk_iot.types.audit_finding_severity.deserialize_json(
            data["severity"]
        )
    if "nonCompliantResource" in data:
        import aws_sdk_iot.types.non_compliant_resource

        out["non_compliant_resource"] = (
            aws_sdk_iot.types.non_compliant_resource.deserialize_json(
                data["nonCompliantResource"]
            )
        )
    if "relatedResources" in data:
        import aws_sdk_iot.types.related_resources

        out["related_resources"] = aws_sdk_iot.types.related_resources.deserialize_json(
            data["relatedResources"]
        )
    if "reasonForNonCompliance" in data:
        out["reason_for_non_compliance"] = data["reasonForNonCompliance"]
    if "reasonForNonComplianceCode" in data:
        out["reason_for_non_compliance_code"] = data["reasonForNonComplianceCode"]
    if "isSuppressed" in data:
        out["is_suppressed"] = data["isSuppressed"]
    return out
