"""Generated from Smithy shape ``com.amazonaws.connect#RuleAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.action_type
    import aws_sdk_connect.types.assign_contact_category_action_definition
    import aws_sdk_connect.types.assign_sla_action_definition
    import aws_sdk_connect.types.create_case_action_definition
    import aws_sdk_connect.types.end_associated_tasks_action_definition
    import aws_sdk_connect.types.event_bridge_action_definition
    import aws_sdk_connect.types.send_notification_action_definition
    import aws_sdk_connect.types.submit_auto_evaluation_action_definition
    import aws_sdk_connect.types.task_action_definition
    import aws_sdk_connect.types.update_case_action_definition


class RuleAction(TypedDict):
    action_type: "aws_sdk_connect.types.action_type.ActionType"
    """<p>The type of action that creates a rule.</p>"""
    task_action: NotRequired[
        "aws_sdk_connect.types.task_action_definition.TaskActionDefinition"
    ]
    """<p>Information about the task action. This field is required if <code>TriggerEventSource</code> is one of the following values: <code>OnZendeskTicketCreate</code> | <code>OnZendeskTicketStatusUpdate</code> | <code>OnSalesforceCaseCreate</code> </p>"""
    event_bridge_action: NotRequired[
        "aws_sdk_connect.types.event_bridge_action_definition.EventBridgeActionDefinition"
    ]
    """<p>Information about the EventBridge action.</p> <p>Supported only for <code>TriggerEventSource</code> values: <code>OnPostCallAnalysisAvailable</code> | <code>OnRealTimeCallAnalysisAvailable</code> | <code>OnRealTimeChatAnalysisAvailable</code> | <code>OnPostChatAnalysisAvailable</code> | <code>OnContactEvaluationSubmit</code> | <code>OnMetricDataUpdate</code> </p>"""
    assign_contact_category_action: NotRequired[
        "aws_sdk_connect.types.assign_contact_category_action_definition.AssignContactCategoryActionDefinition"
    ]
    """<p>Information about the contact category action.</p> <p>Supported only for <code>TriggerEventSource</code> values: <code>OnPostCallAnalysisAvailable</code> | <code>OnRealTimeCallAnalysisAvailable</code> | <code>OnRealTimeChatAnalysisAvailable</code> | <code>OnPostChatAnalysisAvailable</code> | <code>OnZendeskTicketCreate</code> | <code>OnZendeskTicketStatusUpdate</code> | <code>OnSalesforceCaseCreate</code> </p>"""
    send_notification_action: NotRequired[
        "aws_sdk_connect.types.send_notification_action_definition.SendNotificationActionDefinition"
    ]
    """<p>Information about the send notification action.</p> <p>Supported only for <code>TriggerEventSource</code> values: <code>OnPostCallAnalysisAvailable</code> | <code>OnRealTimeCallAnalysisAvailable</code> | <code>OnRealTimeChatAnalysisAvailable</code> | <code>OnPostChatAnalysisAvailable</code> | <code>OnContactEvaluationSubmit</code> | <code>OnMetricDataUpdate</code> </p>"""
    create_case_action: NotRequired[
        "aws_sdk_connect.types.create_case_action_definition.CreateCaseActionDefinition"
    ]
    """<p>Information about the create case action.</p> <p>Supported only for <code>TriggerEventSource</code> values: <code>OnPostCallAnalysisAvailable</code> | <code>OnPostChatAnalysisAvailable</code>.</p>"""
    update_case_action: NotRequired[
        "aws_sdk_connect.types.update_case_action_definition.UpdateCaseActionDefinition"
    ]
    """<p>Information about the update case action.</p> <p>Supported only for <code>TriggerEventSource</code> values: <code>OnCaseCreate</code> | <code>OnCaseUpdate</code>.</p>"""
    assign_sla_action: NotRequired[
        "aws_sdk_connect.types.assign_sla_action_definition.AssignSlaActionDefinition"
    ]
    """<p>Information about the assign SLA action.</p>"""
    end_associated_tasks_action: NotRequired[
        "aws_sdk_connect.types.end_associated_tasks_action_definition.EndAssociatedTasksActionDefinition"
    ]
    """<p>Information about the end associated tasks action.</p> <p>Supported only for <code>TriggerEventSource</code> values: <code>OnCaseUpdate</code>.</p>"""
    submit_auto_evaluation_action: NotRequired[
        "aws_sdk_connect.types.submit_auto_evaluation_action_definition.SubmitAutoEvaluationActionDefinition"
    ]
    """<p>Information about the submit automated evaluation action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleAction) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.action_type

    out["ActionType"] = aws_sdk_connect.types.action_type.serialize_json(
        value["action_type"]
    )
    if "task_action" in value:
        import aws_sdk_connect.types.task_action_definition

        out["TaskAction"] = aws_sdk_connect.types.task_action_definition.serialize_json(
            value["task_action"]
        )
    if "event_bridge_action" in value:
        import aws_sdk_connect.types.event_bridge_action_definition

        out["EventBridgeAction"] = (
            aws_sdk_connect.types.event_bridge_action_definition.serialize_json(
                value["event_bridge_action"]
            )
        )
    if "assign_contact_category_action" in value:
        import aws_sdk_connect.types.assign_contact_category_action_definition

        out["AssignContactCategoryAction"] = (
            aws_sdk_connect.types.assign_contact_category_action_definition.serialize_json(
                value["assign_contact_category_action"]
            )
        )
    if "send_notification_action" in value:
        import aws_sdk_connect.types.send_notification_action_definition

        out["SendNotificationAction"] = (
            aws_sdk_connect.types.send_notification_action_definition.serialize_json(
                value["send_notification_action"]
            )
        )
    if "create_case_action" in value:
        import aws_sdk_connect.types.create_case_action_definition

        out["CreateCaseAction"] = (
            aws_sdk_connect.types.create_case_action_definition.serialize_json(
                value["create_case_action"]
            )
        )
    if "update_case_action" in value:
        import aws_sdk_connect.types.update_case_action_definition

        out["UpdateCaseAction"] = (
            aws_sdk_connect.types.update_case_action_definition.serialize_json(
                value["update_case_action"]
            )
        )
    if "assign_sla_action" in value:
        import aws_sdk_connect.types.assign_sla_action_definition

        out["AssignSlaAction"] = (
            aws_sdk_connect.types.assign_sla_action_definition.serialize_json(
                value["assign_sla_action"]
            )
        )
    if "end_associated_tasks_action" in value:
        import aws_sdk_connect.types.end_associated_tasks_action_definition

        out["EndAssociatedTasksAction"] = (
            aws_sdk_connect.types.end_associated_tasks_action_definition.serialize_json(
                value["end_associated_tasks_action"]
            )
        )
    if "submit_auto_evaluation_action" in value:
        import aws_sdk_connect.types.submit_auto_evaluation_action_definition

        out["SubmitAutoEvaluationAction"] = (
            aws_sdk_connect.types.submit_auto_evaluation_action_definition.serialize_json(
                value["submit_auto_evaluation_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleAction:
    out: RuleAction = {}  # type: ignore[typeddict-item]
    if "ActionType" in data:
        import aws_sdk_connect.types.action_type

        out["action_type"] = aws_sdk_connect.types.action_type.deserialize_json(
            data["ActionType"]
        )
    else:
        raise DeserializationError("RuleAction.action_type required")
    if "TaskAction" in data:
        import aws_sdk_connect.types.task_action_definition

        out["task_action"] = (
            aws_sdk_connect.types.task_action_definition.deserialize_json(
                data["TaskAction"]
            )
        )
    if "EventBridgeAction" in data:
        import aws_sdk_connect.types.event_bridge_action_definition

        out["event_bridge_action"] = (
            aws_sdk_connect.types.event_bridge_action_definition.deserialize_json(
                data["EventBridgeAction"]
            )
        )
    if "AssignContactCategoryAction" in data:
        import aws_sdk_connect.types.assign_contact_category_action_definition

        out["assign_contact_category_action"] = (
            aws_sdk_connect.types.assign_contact_category_action_definition.deserialize_json(
                data["AssignContactCategoryAction"]
            )
        )
    if "SendNotificationAction" in data:
        import aws_sdk_connect.types.send_notification_action_definition

        out["send_notification_action"] = (
            aws_sdk_connect.types.send_notification_action_definition.deserialize_json(
                data["SendNotificationAction"]
            )
        )
    if "CreateCaseAction" in data:
        import aws_sdk_connect.types.create_case_action_definition

        out["create_case_action"] = (
            aws_sdk_connect.types.create_case_action_definition.deserialize_json(
                data["CreateCaseAction"]
            )
        )
    if "UpdateCaseAction" in data:
        import aws_sdk_connect.types.update_case_action_definition

        out["update_case_action"] = (
            aws_sdk_connect.types.update_case_action_definition.deserialize_json(
                data["UpdateCaseAction"]
            )
        )
    if "AssignSlaAction" in data:
        import aws_sdk_connect.types.assign_sla_action_definition

        out["assign_sla_action"] = (
            aws_sdk_connect.types.assign_sla_action_definition.deserialize_json(
                data["AssignSlaAction"]
            )
        )
    if "EndAssociatedTasksAction" in data:
        import aws_sdk_connect.types.end_associated_tasks_action_definition

        out["end_associated_tasks_action"] = (
            aws_sdk_connect.types.end_associated_tasks_action_definition.deserialize_json(
                data["EndAssociatedTasksAction"]
            )
        )
    if "SubmitAutoEvaluationAction" in data:
        import aws_sdk_connect.types.submit_auto_evaluation_action_definition

        out["submit_auto_evaluation_action"] = (
            aws_sdk_connect.types.submit_auto_evaluation_action_definition.deserialize_json(
                data["SubmitAutoEvaluationAction"]
            )
        )
    return out
