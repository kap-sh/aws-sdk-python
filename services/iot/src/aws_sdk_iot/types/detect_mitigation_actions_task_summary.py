"""Generated from Smithy shape ``com.amazonaws.iot#DetectMitigationActionsTaskSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.detect_mitigation_actions_task_statistics
    import aws_sdk_iot.types.detect_mitigation_actions_task_status
    import aws_sdk_iot.types.detect_mitigation_actions_task_target
    import aws_sdk_iot.types.mitigation_action_list
    import aws_sdk_iot.types.mitigation_actions_task_id
    import aws_sdk_iot.types.primitive_boolean
    import aws_sdk_iot.types.timestamp
    import aws_sdk_iot.types.violation_event_occurrence_range


class DetectMitigationActionsTaskSummary(TypedDict, closed=True):
    task_id: NotRequired[
        "aws_sdk_iot.types.mitigation_actions_task_id.MitigationActionsTaskId"
    ]
    """<p> The unique identifier of the task. </p>"""
    task_status: NotRequired[
        "aws_sdk_iot.types.detect_mitigation_actions_task_status.DetectMitigationActionsTaskStatus"
    ]
    """<p> The status of the task. </p>"""
    task_start_time: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p> The date the task started. </p>"""
    task_end_time: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p> The date the task ended. </p>"""
    target: NotRequired[
        "aws_sdk_iot.types.detect_mitigation_actions_task_target.DetectMitigationActionsTaskTarget"
    ]
    """<p> Specifies the ML Detect findings to which the mitigation actions are applied. </p>"""
    violation_event_occurrence_range: NotRequired[
        "aws_sdk_iot.types.violation_event_occurrence_range.ViolationEventOccurrenceRange"
    ]
    """<p> Specifies the time period of which violation events occurred between. </p>"""
    only_active_violations_included: (
        "aws_sdk_iot.types.primitive_boolean.PrimitiveBoolean"
    )
    """<p> Includes only active violations. </p>"""
    suppressed_alerts_included: "aws_sdk_iot.types.primitive_boolean.PrimitiveBoolean"
    """<p> Includes suppressed alerts. </p>"""
    actions_definition: NotRequired[
        "aws_sdk_iot.types.mitigation_action_list.MitigationActionList"
    ]
    """<p> The definition of the actions. </p>"""
    task_statistics: NotRequired[
        "aws_sdk_iot.types.detect_mitigation_actions_task_statistics.DetectMitigationActionsTaskStatistics"
    ]
    """<p> The statistics of a mitigation action task. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectMitigationActionsTaskSummary) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "task_status" in value:
        import aws_sdk_iot.types.detect_mitigation_actions_task_status

        out["taskStatus"] = (
            aws_sdk_iot.types.detect_mitigation_actions_task_status.serialize_json(
                value["task_status"]
            )
        )
    if "task_start_time" in value:
        import aws_sdk_iot.types.timestamp

        out["taskStartTime"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["task_start_time"]
        )
    if "task_end_time" in value:
        import aws_sdk_iot.types.timestamp

        out["taskEndTime"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["task_end_time"]
        )
    if "target" in value:
        import aws_sdk_iot.types.detect_mitigation_actions_task_target

        out["target"] = (
            aws_sdk_iot.types.detect_mitigation_actions_task_target.serialize_json(
                value["target"]
            )
        )
    if "violation_event_occurrence_range" in value:
        import aws_sdk_iot.types.violation_event_occurrence_range

        out["violationEventOccurrenceRange"] = (
            aws_sdk_iot.types.violation_event_occurrence_range.serialize_json(
                value["violation_event_occurrence_range"]
            )
        )
    out["onlyActiveViolationsIncluded"] = value.get(
        "only_active_violations_included", False
    )
    out["suppressedAlertsIncluded"] = value.get("suppressed_alerts_included", False)
    if "actions_definition" in value:
        import aws_sdk_iot.types.mitigation_action_list

        out["actionsDefinition"] = (
            aws_sdk_iot.types.mitigation_action_list.serialize_json(
                value["actions_definition"]
            )
        )
    if "task_statistics" in value:
        import aws_sdk_iot.types.detect_mitigation_actions_task_statistics

        out["taskStatistics"] = (
            aws_sdk_iot.types.detect_mitigation_actions_task_statistics.serialize_json(
                value["task_statistics"]
            )
        )
    return out


def deserialize_json(data: dict) -> DetectMitigationActionsTaskSummary:
    out: DetectMitigationActionsTaskSummary = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "taskStatus" in data:
        import aws_sdk_iot.types.detect_mitigation_actions_task_status

        out["task_status"] = (
            aws_sdk_iot.types.detect_mitigation_actions_task_status.deserialize_json(
                data["taskStatus"]
            )
        )
    if "taskStartTime" in data:
        import aws_sdk_iot.types.timestamp

        out["task_start_time"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["taskStartTime"]
        )
    if "taskEndTime" in data:
        import aws_sdk_iot.types.timestamp

        out["task_end_time"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["taskEndTime"]
        )
    if "target" in data:
        import aws_sdk_iot.types.detect_mitigation_actions_task_target

        out["target"] = (
            aws_sdk_iot.types.detect_mitigation_actions_task_target.deserialize_json(
                data["target"]
            )
        )
    if "violationEventOccurrenceRange" in data:
        import aws_sdk_iot.types.violation_event_occurrence_range

        out["violation_event_occurrence_range"] = (
            aws_sdk_iot.types.violation_event_occurrence_range.deserialize_json(
                data["violationEventOccurrenceRange"]
            )
        )
    if "onlyActiveViolationsIncluded" in data:
        out["only_active_violations_included"] = data["onlyActiveViolationsIncluded"]
    else:
        out["only_active_violations_included"] = False
    if "suppressedAlertsIncluded" in data:
        out["suppressed_alerts_included"] = data["suppressedAlertsIncluded"]
    else:
        out["suppressed_alerts_included"] = False
    if "actionsDefinition" in data:
        import aws_sdk_iot.types.mitigation_action_list

        out["actions_definition"] = (
            aws_sdk_iot.types.mitigation_action_list.deserialize_json(
                data["actionsDefinition"]
            )
        )
    if "taskStatistics" in data:
        import aws_sdk_iot.types.detect_mitigation_actions_task_statistics

        out["task_statistics"] = (
            aws_sdk_iot.types.detect_mitigation_actions_task_statistics.deserialize_json(
                data["taskStatistics"]
            )
        )
    return out
