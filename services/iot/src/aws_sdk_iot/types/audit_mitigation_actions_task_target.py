"""Generated from Smithy shape ``com.amazonaws.iot#AuditMitigationActionsTaskTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_check_to_reason_code_filter
    import aws_sdk_iot.types.audit_task_id
    import aws_sdk_iot.types.finding_ids


class AuditMitigationActionsTaskTarget(TypedDict):
    audit_task_id: NotRequired["aws_sdk_iot.types.audit_task_id.AuditTaskId"]
    """<p>If the task will apply a mitigation action to findings from a specific audit, this value uniquely identifies the audit.</p>"""
    finding_ids: NotRequired["aws_sdk_iot.types.finding_ids.FindingIds"]
    """<p>If the task will apply a mitigation action to one or more listed findings, this value uniquely identifies those findings.</p>"""
    audit_check_to_reason_code_filter: NotRequired[
        "aws_sdk_iot.types.audit_check_to_reason_code_filter.AuditCheckToReasonCodeFilter"
    ]
    """<p>Specifies a filter in the form of an audit check and set of reason codes that identify the findings from the audit to which the audit mitigation actions task apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditMitigationActionsTaskTarget) -> dict:
    out: dict = {}
    if "audit_task_id" in value:
        out["auditTaskId"] = value["audit_task_id"]
    if "finding_ids" in value:
        import aws_sdk_iot.types.finding_ids

        out["findingIds"] = aws_sdk_iot.types.finding_ids.serialize_json(
            value["finding_ids"]
        )
    if "audit_check_to_reason_code_filter" in value:
        import aws_sdk_iot.types.audit_check_to_reason_code_filter

        out["auditCheckToReasonCodeFilter"] = (
            aws_sdk_iot.types.audit_check_to_reason_code_filter.serialize_json(
                value["audit_check_to_reason_code_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuditMitigationActionsTaskTarget:
    out: AuditMitigationActionsTaskTarget = {}  # type: ignore[typeddict-item]
    if "auditTaskId" in data:
        out["audit_task_id"] = data["auditTaskId"]
    if "findingIds" in data:
        import aws_sdk_iot.types.finding_ids

        out["finding_ids"] = aws_sdk_iot.types.finding_ids.deserialize_json(
            data["findingIds"]
        )
    if "auditCheckToReasonCodeFilter" in data:
        import aws_sdk_iot.types.audit_check_to_reason_code_filter

        out["audit_check_to_reason_code_filter"] = (
            aws_sdk_iot.types.audit_check_to_reason_code_filter.deserialize_json(
                data["auditCheckToReasonCodeFilter"]
            )
        )
    return out
