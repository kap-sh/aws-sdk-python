"""Generated from Smithy shape ``com.amazonaws.deadline#CreateQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.allowed_storage_profile_ids
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.default_queue_budget_action
    import aws_sdk_deadline.types.description
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.iam_role_arn
    import aws_sdk_deadline.types.job_attachment_settings
    import aws_sdk_deadline.types.job_run_as_user
    import aws_sdk_deadline.types.required_file_system_location_names
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.scheduling_configuration
    import aws_sdk_deadline.types.tags


class CreateQueueRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm to connect to the queue.</p>"""
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    display_name: "aws_sdk_deadline.types.resource_name.ResourceName"
    """<p>The display name of the queue.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    description: "aws_sdk_deadline.types.description.Description"
    """<p>The description of the queue.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    default_budget_action: (
        "aws_sdk_deadline.types.default_queue_budget_action.DefaultQueueBudgetAction"
    )
    """<p>The default action to take on a queue if a budget isn't configured.</p>"""
    job_attachment_settings: NotRequired[
        "aws_sdk_deadline.types.job_attachment_settings.JobAttachmentSettings"
    ]
    """<p>The job attachment settings for the queue. These are the Amazon S3 bucket name and the Amazon S3 prefix.</p>"""
    role_arn: NotRequired["aws_sdk_deadline.types.iam_role_arn.IamRoleArn"]
    """<p>The IAM role ARN that workers will use while running jobs for this queue.</p>"""
    job_run_as_user: NotRequired["aws_sdk_deadline.types.job_run_as_user.JobRunAsUser"]
    """<p>The jobs in the queue run as the specified POSIX user.</p>"""
    required_file_system_location_names: NotRequired[
        "aws_sdk_deadline.types.required_file_system_location_names.RequiredFileSystemLocationNames"
    ]
    """<p>The file system location name to include in the queue.</p>"""
    allowed_storage_profile_ids: NotRequired[
        "aws_sdk_deadline.types.allowed_storage_profile_ids.AllowedStorageProfileIds"
    ]
    """<p>The storage profile IDs to include in the queue.</p>"""
    tags: NotRequired["aws_sdk_deadline.types.tags.Tags"]
    """<p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>"""
    scheduling_configuration: NotRequired[
        "aws_sdk_deadline.types.scheduling_configuration.SchedulingConfiguration"
    ]
    """<p>The scheduling configuration for the queue. This configuration determines how workers are assigned to jobs in the queue.</p> <p>If not specified, the queue defaults to the <code>priorityFifo</code> scheduling configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQueueRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    out["description"] = value.get("description", "")
    import aws_sdk_deadline.types.default_queue_budget_action

    out["defaultBudgetAction"] = (
        aws_sdk_deadline.types.default_queue_budget_action.serialize_json(
            value.get("default_budget_action", "NONE")
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
    if "required_file_system_location_names" in value:
        import aws_sdk_deadline.types.required_file_system_location_names

        out["requiredFileSystemLocationNames"] = (
            aws_sdk_deadline.types.required_file_system_location_names.serialize_json(
                value["required_file_system_location_names"]
            )
        )
    if "allowed_storage_profile_ids" in value:
        import aws_sdk_deadline.types.allowed_storage_profile_ids

        out["allowedStorageProfileIds"] = (
            aws_sdk_deadline.types.allowed_storage_profile_ids.serialize_json(
                value["allowed_storage_profile_ids"]
            )
        )
    if "tags" in value:
        import aws_sdk_deadline.types.tags

        out["tags"] = aws_sdk_deadline.types.tags.serialize_json(value["tags"])
    if "scheduling_configuration" in value:
        import aws_sdk_deadline.types.scheduling_configuration

        out["schedulingConfiguration"] = (
            aws_sdk_deadline.types.scheduling_configuration.serialize_json(
                value["scheduling_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateQueueRequest:
    out: CreateQueueRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreateQueueRequest.display_name required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if "defaultBudgetAction" in data:
        import aws_sdk_deadline.types.default_queue_budget_action

        out["default_budget_action"] = (
            aws_sdk_deadline.types.default_queue_budget_action.deserialize_json(
                data["defaultBudgetAction"]
            )
        )
    else:
        out["default_budget_action"] = "NONE"
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
    if "requiredFileSystemLocationNames" in data:
        import aws_sdk_deadline.types.required_file_system_location_names

        out["required_file_system_location_names"] = (
            aws_sdk_deadline.types.required_file_system_location_names.deserialize_json(
                data["requiredFileSystemLocationNames"]
            )
        )
    if "allowedStorageProfileIds" in data:
        import aws_sdk_deadline.types.allowed_storage_profile_ids

        out["allowed_storage_profile_ids"] = (
            aws_sdk_deadline.types.allowed_storage_profile_ids.deserialize_json(
                data["allowedStorageProfileIds"]
            )
        )
    if "tags" in data:
        import aws_sdk_deadline.types.tags

        out["tags"] = aws_sdk_deadline.types.tags.deserialize_json(data["tags"])
    if "schedulingConfiguration" in data:
        import aws_sdk_deadline.types.scheduling_configuration

        out["scheduling_configuration"] = (
            aws_sdk_deadline.types.scheduling_configuration.deserialize_json(
                data["schedulingConfiguration"]
            )
        )
    return out
