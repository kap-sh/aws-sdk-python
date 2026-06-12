"""Generated from Smithy shape ``com.amazonaws.deadline#AssignedSessionActionDefinition``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.assigned_environment_enter_session_action_definition
    import aws_sdk_deadline.types.assigned_environment_exit_session_action_definition
    import aws_sdk_deadline.types.assigned_sync_input_job_attachments_session_action_definition
    import aws_sdk_deadline.types.assigned_task_run_session_action_definition


class _AssignedSessionActionDefinition_envEnter(TypedDict):
    envEnter: "aws_sdk_deadline.types.assigned_environment_enter_session_action_definition.AssignedEnvironmentEnterSessionActionDefinition"


class _AssignedSessionActionDefinition_envExit(TypedDict):
    envExit: "aws_sdk_deadline.types.assigned_environment_exit_session_action_definition.AssignedEnvironmentExitSessionActionDefinition"


class _AssignedSessionActionDefinition_taskRun(TypedDict):
    taskRun: "aws_sdk_deadline.types.assigned_task_run_session_action_definition.AssignedTaskRunSessionActionDefinition"


class _AssignedSessionActionDefinition_syncInputJobAttachments(TypedDict):
    syncInputJobAttachments: "aws_sdk_deadline.types.assigned_sync_input_job_attachments_session_action_definition.AssignedSyncInputJobAttachmentsSessionActionDefinition"


AssignedSessionActionDefinition: TypeAlias = (
    _AssignedSessionActionDefinition_envEnter
    | _AssignedSessionActionDefinition_envExit
    | _AssignedSessionActionDefinition_taskRun
    | _AssignedSessionActionDefinition_syncInputJobAttachments
)


# --- restJson1 ser/de ---
def serialize_json(value: AssignedSessionActionDefinition) -> dict:
    if "envEnter" in value:
        import aws_sdk_deadline.types.assigned_environment_enter_session_action_definition

        return {
            "envEnter": aws_sdk_deadline.types.assigned_environment_enter_session_action_definition.serialize_json(
                value["envEnter"]
            )
        }
    elif "envExit" in value:
        import aws_sdk_deadline.types.assigned_environment_exit_session_action_definition

        return {
            "envExit": aws_sdk_deadline.types.assigned_environment_exit_session_action_definition.serialize_json(
                value["envExit"]
            )
        }
    elif "taskRun" in value:
        import aws_sdk_deadline.types.assigned_task_run_session_action_definition

        return {
            "taskRun": aws_sdk_deadline.types.assigned_task_run_session_action_definition.serialize_json(
                value["taskRun"]
            )
        }
    elif "syncInputJobAttachments" in value:
        import aws_sdk_deadline.types.assigned_sync_input_job_attachments_session_action_definition

        return {
            "syncInputJobAttachments": aws_sdk_deadline.types.assigned_sync_input_job_attachments_session_action_definition.serialize_json(
                value["syncInputJobAttachments"]
            )
        }
    else:
        raise SerializationError("AssignedSessionActionDefinition: no variant present")


def deserialize_json(data: dict) -> AssignedSessionActionDefinition:
    if "envEnter" in data:
        import aws_sdk_deadline.types.assigned_environment_enter_session_action_definition

        return {
            "envEnter": aws_sdk_deadline.types.assigned_environment_enter_session_action_definition.deserialize_json(
                data["envEnter"]
            )
        }
    elif "envExit" in data:
        import aws_sdk_deadline.types.assigned_environment_exit_session_action_definition

        return {
            "envExit": aws_sdk_deadline.types.assigned_environment_exit_session_action_definition.deserialize_json(
                data["envExit"]
            )
        }
    elif "taskRun" in data:
        import aws_sdk_deadline.types.assigned_task_run_session_action_definition

        return {
            "taskRun": aws_sdk_deadline.types.assigned_task_run_session_action_definition.deserialize_json(
                data["taskRun"]
            )
        }
    elif "syncInputJobAttachments" in data:
        import aws_sdk_deadline.types.assigned_sync_input_job_attachments_session_action_definition

        return {
            "syncInputJobAttachments": aws_sdk_deadline.types.assigned_sync_input_job_attachments_session_action_definition.deserialize_json(
                data["syncInputJobAttachments"]
            )
        }
    else:
        raise DeserializationError(
            "AssignedSessionActionDefinition: no recognized variant key"
        )
