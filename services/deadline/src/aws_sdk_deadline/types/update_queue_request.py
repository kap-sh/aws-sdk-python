"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateQueueRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.allowed_storage_profile_ids
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.default_queue_budget_action
    import aws_sdk_deadline.types.description
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.iam_role_arn
    import aws_sdk_deadline.types.job_attachment_settings
    import aws_sdk_deadline.types.job_run_as_user
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.required_file_system_location_names
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.scheduling_configuration


class UpdateQueueRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID to update in the queue.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID to update.</p>"""
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The idempotency token to update in the queue.</p>"""
    display_name: NotRequired["aws_sdk_deadline.types.resource_name.ResourceName"]
    """<p>The display name of the queue to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    description: NotRequired["aws_sdk_deadline.types.description.Description"]
    """<p>The description of the queue to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    default_budget_action: NotRequired[
        "aws_sdk_deadline.types.default_queue_budget_action.DefaultQueueBudgetAction"
    ]
    """<p>The default action to take for a queue update if a budget isn't configured.</p>"""
    job_attachment_settings: NotRequired[
        "aws_sdk_deadline.types.job_attachment_settings.JobAttachmentSettings"
    ]
    """<p>The job attachment settings to update for the queue.</p>"""
    role_arn: NotRequired["aws_sdk_deadline.types.iam_role_arn.IamRoleArn"]
    """<p>The IAM role ARN that's used to run jobs from this queue.</p>"""
    job_run_as_user: NotRequired["aws_sdk_deadline.types.job_run_as_user.JobRunAsUser"]
    """<p>Update the jobs in the queue to run as a specified POSIX user.</p>"""
    required_file_system_location_names_to_add: NotRequired[
        "aws_sdk_deadline.types.required_file_system_location_names.RequiredFileSystemLocationNames"
    ]
    """<p>The required file system location names to add to the queue.</p>"""
    required_file_system_location_names_to_remove: NotRequired[
        "aws_sdk_deadline.types.required_file_system_location_names.RequiredFileSystemLocationNames"
    ]
    """<p>The required file system location names to remove from the queue.</p>"""
    allowed_storage_profile_ids_to_add: NotRequired[
        "aws_sdk_deadline.types.allowed_storage_profile_ids.AllowedStorageProfileIds"
    ]
    """<p>The storage profile IDs to add.</p>"""
    allowed_storage_profile_ids_to_remove: NotRequired[
        "aws_sdk_deadline.types.allowed_storage_profile_ids.AllowedStorageProfileIds"
    ]
    """<p>The storage profile ID to remove.</p>"""
    scheduling_configuration: NotRequired[
        "aws_sdk_deadline.types.scheduling_configuration.SchedulingConfiguration"
    ]
    """<p>The scheduling configuration for the queue. This configuration determines how workers are assigned to jobs in the queue.</p> <p>When updating the scheduling configuration, the entire configuration is replaced.</p> <p>In-progress tasks run to completion before the new scheduling configuration takes effect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "default_budget_action" in value:
        import aws_sdk_deadline.types.default_queue_budget_action

        out["defaultBudgetAction"] = (
            aws_sdk_deadline.types.default_queue_budget_action.serialize_json(
                value["default_budget_action"]
            )
        )
    if "job_attachment_settings" in value:
        import aws_sdk_deadline.types.job_attachment_settings

        out["jobAttachmentSettings"] = (
            aws_sdk_deadline.types.job_attachment_settings.serialize_json(
                value["job_attachment_settings"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "job_run_as_user" in value:
        import aws_sdk_deadline.types.job_run_as_user

        out["jobRunAsUser"] = aws_sdk_deadline.types.job_run_as_user.serialize_json(
            value["job_run_as_user"]
        )
    if "required_file_system_location_names_to_add" in value:
        import aws_sdk_deadline.types.required_file_system_location_names

        out["requiredFileSystemLocationNamesToAdd"] = (
            aws_sdk_deadline.types.required_file_system_location_names.serialize_json(
                value["required_file_system_location_names_to_add"]
            )
        )
    if "required_file_system_location_names_to_remove" in value:
        import aws_sdk_deadline.types.required_file_system_location_names

        out["requiredFileSystemLocationNamesToRemove"] = (
            aws_sdk_deadline.types.required_file_system_location_names.serialize_json(
                value["required_file_system_location_names_to_remove"]
            )
        )
    if "allowed_storage_profile_ids_to_add" in value:
        import aws_sdk_deadline.types.allowed_storage_profile_ids

        out["allowedStorageProfileIdsToAdd"] = (
            aws_sdk_deadline.types.allowed_storage_profile_ids.serialize_json(
                value["allowed_storage_profile_ids_to_add"]
            )
        )
    if "allowed_storage_profile_ids_to_remove" in value:
        import aws_sdk_deadline.types.allowed_storage_profile_ids

        out["allowedStorageProfileIdsToRemove"] = (
            aws_sdk_deadline.types.allowed_storage_profile_ids.serialize_json(
                value["allowed_storage_profile_ids_to_remove"]
            )
        )
    if "scheduling_configuration" in value:
        import aws_sdk_deadline.types.scheduling_configuration

        out["schedulingConfiguration"] = (
            aws_sdk_deadline.types.scheduling_configuration.serialize_json(
                value["scheduling_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateQueueRequest:
    out: UpdateQueueRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "defaultBudgetAction" in data:
        import aws_sdk_deadline.types.default_queue_budget_action

        out["default_budget_action"] = (
            aws_sdk_deadline.types.default_queue_budget_action.deserialize_json(
                data["defaultBudgetAction"]
            )
        )
    if "jobAttachmentSettings" in data:
        import aws_sdk_deadline.types.job_attachment_settings

        out["job_attachment_settings"] = (
            aws_sdk_deadline.types.job_attachment_settings.deserialize_json(
                data["jobAttachmentSettings"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "jobRunAsUser" in data:
        import aws_sdk_deadline.types.job_run_as_user

        out["job_run_as_user"] = (
            aws_sdk_deadline.types.job_run_as_user.deserialize_json(
                data["jobRunAsUser"]
            )
        )
    if "requiredFileSystemLocationNamesToAdd" in data:
        import aws_sdk_deadline.types.required_file_system_location_names

        out["required_file_system_location_names_to_add"] = (
            aws_sdk_deadline.types.required_file_system_location_names.deserialize_json(
                data["requiredFileSystemLocationNamesToAdd"]
            )
        )
    if "requiredFileSystemLocationNamesToRemove" in data:
        import aws_sdk_deadline.types.required_file_system_location_names

        out["required_file_system_location_names_to_remove"] = (
            aws_sdk_deadline.types.required_file_system_location_names.deserialize_json(
                data["requiredFileSystemLocationNamesToRemove"]
            )
        )
    if "allowedStorageProfileIdsToAdd" in data:
        import aws_sdk_deadline.types.allowed_storage_profile_ids

        out["allowed_storage_profile_ids_to_add"] = (
            aws_sdk_deadline.types.allowed_storage_profile_ids.deserialize_json(
                data["allowedStorageProfileIdsToAdd"]
            )
        )
    if "allowedStorageProfileIdsToRemove" in data:
        import aws_sdk_deadline.types.allowed_storage_profile_ids

        out["allowed_storage_profile_ids_to_remove"] = (
            aws_sdk_deadline.types.allowed_storage_profile_ids.deserialize_json(
                data["allowedStorageProfileIdsToRemove"]
            )
        )
    if "schedulingConfiguration" in data:
        import aws_sdk_deadline.types.scheduling_configuration

        out["scheduling_configuration"] = (
            aws_sdk_deadline.types.scheduling_configuration.deserialize_json(
                data["schedulingConfiguration"]
            )
        )
    return out
