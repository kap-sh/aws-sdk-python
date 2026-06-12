"""Generated from Smithy shape ``com.amazonaws.deadline#SessionActionDefinitionSummary``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.environment_enter_session_action_definition_summary
    import aws_sdk_deadline.types.environment_exit_session_action_definition_summary
    import aws_sdk_deadline.types.sync_input_job_attachments_session_action_definition_summary
    import aws_sdk_deadline.types.task_run_session_action_definition_summary


class _SessionActionDefinitionSummary_envEnter(TypedDict):
    envEnter: "aws_sdk_deadline.types.environment_enter_session_action_definition_summary.EnvironmentEnterSessionActionDefinitionSummary"


class _SessionActionDefinitionSummary_envExit(TypedDict):
    envExit: "aws_sdk_deadline.types.environment_exit_session_action_definition_summary.EnvironmentExitSessionActionDefinitionSummary"


class _SessionActionDefinitionSummary_taskRun(TypedDict):
    taskRun: "aws_sdk_deadline.types.task_run_session_action_definition_summary.TaskRunSessionActionDefinitionSummary"


class _SessionActionDefinitionSummary_syncInputJobAttachments(TypedDict):
    syncInputJobAttachments: "aws_sdk_deadline.types.sync_input_job_attachments_session_action_definition_summary.SyncInputJobAttachmentsSessionActionDefinitionSummary"


SessionActionDefinitionSummary: TypeAlias = (
    _SessionActionDefinitionSummary_envEnter
    | _SessionActionDefinitionSummary_envExit
    | _SessionActionDefinitionSummary_taskRun
    | _SessionActionDefinitionSummary_syncInputJobAttachments
)


# --- restJson1 ser/de ---
def serialize_json(value: SessionActionDefinitionSummary) -> dict:
    if "envEnter" in value:
        import aws_sdk_deadline.types.environment_enter_session_action_definition_summary

        return {
            "envEnter": aws_sdk_deadline.types.environment_enter_session_action_definition_summary.serialize_json(
                value["envEnter"]
            )
        }
    elif "envExit" in value:
        import aws_sdk_deadline.types.environment_exit_session_action_definition_summary

        return {
            "envExit": aws_sdk_deadline.types.environment_exit_session_action_definition_summary.serialize_json(
                value["envExit"]
            )
        }
    elif "taskRun" in value:
        import aws_sdk_deadline.types.task_run_session_action_definition_summary

        return {
            "taskRun": aws_sdk_deadline.types.task_run_session_action_definition_summary.serialize_json(
                value["taskRun"]
            )
        }
    elif "syncInputJobAttachments" in value:
        import aws_sdk_deadline.types.sync_input_job_attachments_session_action_definition_summary

        return {
            "syncInputJobAttachments": aws_sdk_deadline.types.sync_input_job_attachments_session_action_definition_summary.serialize_json(
                value["syncInputJobAttachments"]
            )
        }
    else:
        raise SerializationError("SessionActionDefinitionSummary: no variant present")


def deserialize_json(data: dict) -> SessionActionDefinitionSummary:
    if "envEnter" in data:
        import aws_sdk_deadline.types.environment_enter_session_action_definition_summary

        return {
            "envEnter": aws_sdk_deadline.types.environment_enter_session_action_definition_summary.deserialize_json(
                data["envEnter"]
            )
        }
    elif "envExit" in data:
        import aws_sdk_deadline.types.environment_exit_session_action_definition_summary

        return {
            "envExit": aws_sdk_deadline.types.environment_exit_session_action_definition_summary.deserialize_json(
                data["envExit"]
            )
        }
    elif "taskRun" in data:
        import aws_sdk_deadline.types.task_run_session_action_definition_summary

        return {
            "taskRun": aws_sdk_deadline.types.task_run_session_action_definition_summary.deserialize_json(
                data["taskRun"]
            )
        }
    elif "syncInputJobAttachments" in data:
        import aws_sdk_deadline.types.sync_input_job_attachments_session_action_definition_summary

        return {
            "syncInputJobAttachments": aws_sdk_deadline.types.sync_input_job_attachments_session_action_definition_summary.deserialize_json(
                data["syncInputJobAttachments"]
            )
        }
    else:
        raise DeserializationError(
            "SessionActionDefinitionSummary: no recognized variant key"
        )
