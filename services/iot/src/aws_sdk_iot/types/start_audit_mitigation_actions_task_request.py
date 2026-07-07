"""Generated from Smithy shape ``com.amazonaws.iot#StartAuditMitigationActionsTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_check_to_actions_mapping
    import aws_sdk_iot.types.audit_mitigation_actions_task_target
    import aws_sdk_iot.types.client_request_token
    import aws_sdk_iot.types.mitigation_actions_task_id


class StartAuditMitigationActionsTaskRequest(TypedDict, closed=True):
    task_id: "aws_sdk_iot.types.mitigation_actions_task_id.MitigationActionsTaskId"
    """<p>A unique identifier for the task. You can use this identifier to check the status of the task or to cancel it.</p>"""
    target: "aws_sdk_iot.types.audit_mitigation_actions_task_target.AuditMitigationActionsTaskTarget"
    """<p>Specifies the audit findings to which the mitigation actions are applied. You can apply them to a type of audit check, to all findings from an audit, or to a specific set of findings.</p>"""
    audit_check_to_actions_mapping: (
        "aws_sdk_iot.types.audit_check_to_actions_mapping.AuditCheckToActionsMapping"
    )
    """<p>For an audit check, specifies which mitigation actions to apply. Those actions must be defined in your Amazon Web Services accounts.</p>"""
    client_request_token: "aws_sdk_iot.types.client_request_token.ClientRequestToken"
    """<p>Each audit mitigation task must have a unique client request token. If you try to start a new task with the same token as a task that already exists, an exception occurs. If you omit this value, a unique client request token is generated automatically.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAuditMitigationActionsTaskRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.audit_mitigation_actions_task_target

    out["target"] = (
        aws_sdk_iot.types.audit_mitigation_actions_task_target.serialize_json(
            value["target"]
        )
    )
    import aws_sdk_iot.types.audit_check_to_actions_mapping

    out["auditCheckToActionsMapping"] = (
        aws_sdk_iot.types.audit_check_to_actions_mapping.serialize_json(
            value["audit_check_to_actions_mapping"]
        )
    )
    out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> StartAuditMitigationActionsTaskRequest:
    out: StartAuditMitigationActionsTaskRequest = {}  # type: ignore[typeddict-item]
    if "target" in data:
        import aws_sdk_iot.types.audit_mitigation_actions_task_target

        out["target"] = (
            aws_sdk_iot.types.audit_mitigation_actions_task_target.deserialize_json(
                data["target"]
            )
        )
    else:
        raise DeserializationError(
            "StartAuditMitigationActionsTaskRequest.target required"
        )
    if "auditCheckToActionsMapping" in data:
        import aws_sdk_iot.types.audit_check_to_actions_mapping

        out["audit_check_to_actions_mapping"] = (
            aws_sdk_iot.types.audit_check_to_actions_mapping.deserialize_json(
                data["auditCheckToActionsMapping"]
            )
        )
    else:
        raise DeserializationError(
            "StartAuditMitigationActionsTaskRequest.audit_check_to_actions_mapping required"
        )
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    else:
        raise DeserializationError(
            "StartAuditMitigationActionsTaskRequest.client_request_token required"
        )
    return out
