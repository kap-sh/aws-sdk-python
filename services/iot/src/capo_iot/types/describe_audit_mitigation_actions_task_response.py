"""Generated from Smithy shape ``com.amazonaws.iot#DescribeAuditMitigationActionsTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.audit_check_to_actions_mapping
    import capo_iot.types.audit_mitigation_actions_task_statistics
    import capo_iot.types.audit_mitigation_actions_task_status
    import capo_iot.types.audit_mitigation_actions_task_target
    import capo_iot.types.mitigation_action_list
    import capo_iot.types.timestamp


class DescribeAuditMitigationActionsTaskResponse(TypedDict, closed=True):
    task_status: NotRequired[
        "capo_iot.types.audit_mitigation_actions_task_status.AuditMitigationActionsTaskStatus"
    ]
    """<p>The current status of the task.</p>"""
    start_time: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p>The date and time when the task was started.</p>"""
    end_time: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p>The date and time when the task was completed or canceled.</p>"""
    task_statistics: NotRequired[
        "capo_iot.types.audit_mitigation_actions_task_statistics.AuditMitigationActionsTaskStatistics"
    ]
    """<p>Aggregate counts of the results when the mitigation tasks were applied to the findings for this audit mitigation actions task.</p>"""
    target: NotRequired[
        "capo_iot.types.audit_mitigation_actions_task_target.AuditMitigationActionsTaskTarget"
    ]
    """<p>Identifies the findings to which the mitigation actions are applied. This can be by audit checks, by audit task, or a set of findings.</p>"""
    audit_check_to_actions_mapping: NotRequired[
        "capo_iot.types.audit_check_to_actions_mapping.AuditCheckToActionsMapping"
    ]
    """<p>Specifies the mitigation actions that should be applied to specific audit checks.</p>"""
    actions_definition: NotRequired[
        "capo_iot.types.mitigation_action_list.MitigationActionList"
    ]
    """<p>Specifies the mitigation actions and their parameters that are applied as part of this task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAuditMitigationActionsTaskResponse) -> dict:
    out: dict = {}
    if "task_status" in value:
        import capo_iot.types.audit_mitigation_actions_task_status

        out["taskStatus"] = (
            capo_iot.types.audit_mitigation_actions_task_status.serialize_json(
                value["task_status"]
            )
        )
    if "start_time" in value:
        import capo_iot.types.timestamp

        out["startTime"] = capo_iot.types.timestamp.serialize_json(value["start_time"])
    if "end_time" in value:
        import capo_iot.types.timestamp

        out["endTime"] = capo_iot.types.timestamp.serialize_json(value["end_time"])
    if "task_statistics" in value:
        import capo_iot.types.audit_mitigation_actions_task_statistics

        out["taskStatistics"] = (
            capo_iot.types.audit_mitigation_actions_task_statistics.serialize_json(
                value["task_statistics"]
            )
        )
    if "target" in value:
        import capo_iot.types.audit_mitigation_actions_task_target

        out["target"] = (
            capo_iot.types.audit_mitigation_actions_task_target.serialize_json(
                value["target"]
            )
        )
    if "audit_check_to_actions_mapping" in value:
        import capo_iot.types.audit_check_to_actions_mapping

        out["auditCheckToActionsMapping"] = (
            capo_iot.types.audit_check_to_actions_mapping.serialize_json(
                value["audit_check_to_actions_mapping"]
            )
        )
    if "actions_definition" in value:
        import capo_iot.types.mitigation_action_list

        out["actionsDefinition"] = capo_iot.types.mitigation_action_list.serialize_json(
            value["actions_definition"]
        )
    return out


def deserialize_json(data: dict) -> DescribeAuditMitigationActionsTaskResponse:
    out: DescribeAuditMitigationActionsTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskStatus" in data:
        import capo_iot.types.audit_mitigation_actions_task_status

        out["task_status"] = (
            capo_iot.types.audit_mitigation_actions_task_status.deserialize_json(
                data["taskStatus"]
            )
        )
    if "startTime" in data:
        import capo_iot.types.timestamp

        out["start_time"] = capo_iot.types.timestamp.deserialize_json(data["startTime"])
    if "endTime" in data:
        import capo_iot.types.timestamp

        out["end_time"] = capo_iot.types.timestamp.deserialize_json(data["endTime"])
    if "taskStatistics" in data:
        import capo_iot.types.audit_mitigation_actions_task_statistics

        out["task_statistics"] = (
            capo_iot.types.audit_mitigation_actions_task_statistics.deserialize_json(
                data["taskStatistics"]
            )
        )
    if "target" in data:
        import capo_iot.types.audit_mitigation_actions_task_target

        out["target"] = (
            capo_iot.types.audit_mitigation_actions_task_target.deserialize_json(
                data["target"]
            )
        )
    if "auditCheckToActionsMapping" in data:
        import capo_iot.types.audit_check_to_actions_mapping

        out["audit_check_to_actions_mapping"] = (
            capo_iot.types.audit_check_to_actions_mapping.deserialize_json(
                data["auditCheckToActionsMapping"]
            )
        )
    if "actionsDefinition" in data:
        import capo_iot.types.mitigation_action_list

        out["actions_definition"] = (
            capo_iot.types.mitigation_action_list.deserialize_json(
                data["actionsDefinition"]
            )
        )
    return out
