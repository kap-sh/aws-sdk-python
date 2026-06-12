"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.allowed_storage_profile_ids
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.default_queue_budget_action
    import aws_sdk_deadline.types.description
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.iam_role_arn
    import aws_sdk_deadline.types.job_attachment_settings
    import aws_sdk_deadline.types.job_run_as_user
    import aws_sdk_deadline.types.queue_blocked_reason
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.queue_status
    import aws_sdk_deadline.types.required_file_system_location_names
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.scheduling_configuration
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by


class GetQueueResponse(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the queue.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID.</p>"""
    display_name: "aws_sdk_deadline.types.resource_name.ResourceName"
    """<p>The display name of the queue.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    status: "aws_sdk_deadline.types.queue_status.QueueStatus"
    """<p>The status of the queue.</p> <ul> <li> <p> <code>ACTIVE</code>–The queue is active.</p> </li> <li> <p> <code>SCHEDULING</code>–The queue is scheduling.</p> </li> <li> <p> <code>SCHEDULING_BLOCKED</code>–The queue scheduling is blocked. See the provided reason.</p> </li> </ul>"""
    default_budget_action: (
        "aws_sdk_deadline.types.default_queue_budget_action.DefaultQueueBudgetAction"
    )
    """<p>The default action taken on a queue if a budget wasn't configured.</p>"""
    blocked_reason: NotRequired[
        "aws_sdk_deadline.types.queue_blocked_reason.QueueBlockedReason"
    ]
    """<p>The reason the queue was blocked.</p>"""
    created_at: "aws_sdk_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "aws_sdk_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["aws_sdk_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    description: NotRequired["aws_sdk_deadline.types.description.Description"]
    """<p>The description of the queue.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    job_attachment_settings: NotRequired[
        "aws_sdk_deadline.types.job_attachment_settings.JobAttachmentSettings"
    ]
    """<p>The job attachment settings for the queue.</p>"""
    role_arn: NotRequired["aws_sdk_deadline.types.iam_role_arn.IamRoleArn"]
    """<p>The IAM role ARN.</p>"""
    required_file_system_location_names: NotRequired[
        "aws_sdk_deadline.types.required_file_system_location_names.RequiredFileSystemLocationNames"
    ]
    """<p>A list of the required file system location names in the queue.</p>"""
    allowed_storage_profile_ids: NotRequired[
        "aws_sdk_deadline.types.allowed_storage_profile_ids.AllowedStorageProfileIds"
    ]
    """<p>The storage profile IDs for the queue.</p>"""
    job_run_as_user: NotRequired["aws_sdk_deadline.types.job_run_as_user.JobRunAsUser"]
    """<p>The jobs in the queue ran as this specified POSIX user.</p>"""
    scheduling_configuration: NotRequired[
        "aws_sdk_deadline.types.scheduling_configuration.SchedulingConfiguration"
    ]
    """<p>The scheduling configuration for the queue. This configuration determines how workers are assigned to jobs in the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueResponse) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["displayName"] = value["display_name"]
    import aws_sdk_deadline.types.queue_status

    out["status"] = aws_sdk_deadline.types.queue_status.serialize_json(value["status"])
    import aws_sdk_deadline.types.default_queue_budget_action

    out["defaultBudgetAction"] = (
        aws_sdk_deadline.types.default_queue_budget_action.serialize_json(
            value["default_budget_action"]
        )
    )
    if "blocked_reason" in value:
        import aws_sdk_deadline.types.queue_blocked_reason

        out["blockedReason"] = (
            aws_sdk_deadline.types.queue_blocked_reason.serialize_json(
                value["blocked_reason"]
            )
        )
    import aws_sdk_deadline.types.created_at

    out["createdAt"] = aws_sdk_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import aws_sdk_deadline.types.updated_at

        out["updatedAt"] = aws_sdk_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "description" in value:
        out["description"] = value["description"]
    if "job_attachment_settings" in value:
        import aws_sdk_deadline.types.job_attachment_settings

        out["jobAttachmentSettings"] = (
            aws_sdk_deadline.types.job_attachment_settings.serialize_json(
                value["job_attachment_settings"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
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
    if "job_run_as_user" in value:
        import aws_sdk_deadline.types.job_run_as_user

        out["jobRunAsUser"] = aws_sdk_deadline.types.job_run_as_user.serialize_json(
            value["job_run_as_user"]
        )
    if "scheduling_configuration" in value:
        import aws_sdk_deadline.types.scheduling_configuration

        out["schedulingConfiguration"] = (
            aws_sdk_deadline.types.scheduling_configuration.serialize_json(
                value["scheduling_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetQueueResponse:
    out: GetQueueResponse = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("GetQueueResponse.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("GetQueueResponse.queue_id required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("GetQueueResponse.display_name required")
    if "status" in data:
        import aws_sdk_deadline.types.queue_status

        out["status"] = aws_sdk_deadline.types.queue_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetQueueResponse.status required")
    if "defaultBudgetAction" in data:
        import aws_sdk_deadline.types.default_queue_budget_action

        out["default_budget_action"] = (
            aws_sdk_deadline.types.default_queue_budget_action.deserialize_json(
                data["defaultBudgetAction"]
            )
        )
    else:
        raise DeserializationError("GetQueueResponse.default_budget_action required")
    if "blockedReason" in data:
        import aws_sdk_deadline.types.queue_blocked_reason

        out["blocked_reason"] = (
            aws_sdk_deadline.types.queue_blocked_reason.deserialize_json(
                data["blockedReason"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetQueueResponse.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetQueueResponse.created_by required")
    if "updatedAt" in data:
        import aws_sdk_deadline.types.updated_at

        out["updated_at"] = aws_sdk_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "description" in data:
        out["description"] = data["description"]
    if "jobAttachmentSettings" in data:
        import aws_sdk_deadline.types.job_attachment_settings

        out["job_attachment_settings"] = (
            aws_sdk_deadline.types.job_attachment_settings.deserialize_json(
                data["jobAttachmentSettings"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
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
    if "jobRunAsUser" in data:
        import aws_sdk_deadline.types.job_run_as_user

        out["job_run_as_user"] = (
            aws_sdk_deadline.types.job_run_as_user.deserialize_json(
                data["jobRunAsUser"]
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
