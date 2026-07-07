"""Generated from Smithy shape ``com.amazonaws.deadline#SessionActionDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.environment_enter_session_action_definition
    import aws_sdk_deadline.types.environment_exit_session_action_definition
    import aws_sdk_deadline.types.sync_input_job_attachments_session_action_definition
    import aws_sdk_deadline.types.task_run_session_action_definition


class _SessionActionDefinition_envEnter(TypedDict, closed=True):
    envEnter: "aws_sdk_deadline.types.environment_enter_session_action_definition.EnvironmentEnterSessionActionDefinition"


class _SessionActionDefinition_envExit(TypedDict, closed=True):
    envExit: "aws_sdk_deadline.types.environment_exit_session_action_definition.EnvironmentExitSessionActionDefinition"


class _SessionActionDefinition_taskRun(TypedDict, closed=True):
    taskRun: "aws_sdk_deadline.types.task_run_session_action_definition.TaskRunSessionActionDefinition"


class _SessionActionDefinition_syncInputJobAttachments(TypedDict, closed=True):
    syncInputJobAttachments: "aws_sdk_deadline.types.sync_input_job_attachments_session_action_definition.SyncInputJobAttachmentsSessionActionDefinition"


SessionActionDefinition: TypeAlias = (
    _SessionActionDefinition_envEnter
    | _SessionActionDefinition_envExit
    | _SessionActionDefinition_taskRun
    | _SessionActionDefinition_syncInputJobAttachments
)


# --- restJson1 ser/de ---
def serialize_json(value: SessionActionDefinition) -> dict:
    if "envEnter" in value:
        import aws_sdk_deadline.types.environment_enter_session_action_definition

        return {
            "envEnter": aws_sdk_deadline.types.environment_enter_session_action_definition.serialize_json(
                value["envEnter"]
            )
        }
    elif "envExit" in value:
        import aws_sdk_deadline.types.environment_exit_session_action_definition

        return {
            "envExit": aws_sdk_deadline.types.environment_exit_session_action_definition.serialize_json(
                value["envExit"]
            )
        }
    elif "taskRun" in value:
        import aws_sdk_deadline.types.task_run_session_action_definition

        return {
            "taskRun": aws_sdk_deadline.types.task_run_session_action_definition.serialize_json(
                value["taskRun"]
            )
        }
    elif "syncInputJobAttachments" in value:
        import aws_sdk_deadline.types.sync_input_job_attachments_session_action_definition

        return {
            "syncInputJobAttachments": aws_sdk_deadline.types.sync_input_job_attachments_session_action_definition.serialize_json(
                value["syncInputJobAttachments"]
            )
        }
    else:
        raise SerializationError("SessionActionDefinition: no variant present")


def deserialize_json(data: dict) -> SessionActionDefinition:
    if "envEnter" in data:
        import aws_sdk_deadline.types.environment_enter_session_action_definition

        return {
            "envEnter": aws_sdk_deadline.types.environment_enter_session_action_definition.deserialize_json(
                data["envEnter"]
            )
        }
    elif "envExit" in data:
        import aws_sdk_deadline.types.environment_exit_session_action_definition

        return {
            "envExit": aws_sdk_deadline.types.environment_exit_session_action_definition.deserialize_json(
                data["envExit"]
            )
        }
    elif "taskRun" in data:
        import aws_sdk_deadline.types.task_run_session_action_definition

        return {
            "taskRun": aws_sdk_deadline.types.task_run_session_action_definition.deserialize_json(
                data["taskRun"]
            )
        }
    elif "syncInputJobAttachments" in data:
        import aws_sdk_deadline.types.sync_input_job_attachments_session_action_definition

        return {
            "syncInputJobAttachments": aws_sdk_deadline.types.sync_input_job_attachments_session_action_definition.deserialize_json(
                data["syncInputJobAttachments"]
            )
        }
    else:
        raise DeserializationError("SessionActionDefinition: no recognized variant key")
