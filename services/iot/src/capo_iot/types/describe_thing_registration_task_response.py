"""Generated from Smithy shape ``com.amazonaws.iot#DescribeThingRegistrationTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.count
    import capo_iot.types.creation_date
    import capo_iot.types.error_message
    import capo_iot.types.last_modified_date
    import capo_iot.types.percentage
    import capo_iot.types.registry_s3_bucket_name
    import capo_iot.types.registry_s3_key_name
    import capo_iot.types.role_arn
    import capo_iot.types.status
    import capo_iot.types.task_id
    import capo_iot.types.template_body


class DescribeThingRegistrationTaskResponse(TypedDict, closed=True):
    task_id: NotRequired["capo_iot.types.task_id.TaskId"]
    """<p>The task ID.</p>"""
    creation_date: NotRequired["capo_iot.types.creation_date.CreationDate"]
    """<p>The task creation date.</p>"""
    last_modified_date: NotRequired[
        "capo_iot.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date when the task was last modified.</p>"""
    template_body: NotRequired["capo_iot.types.template_body.TemplateBody"]
    """<p>The task's template.</p>"""
    input_file_bucket: NotRequired[
        "capo_iot.types.registry_s3_bucket_name.RegistryS3BucketName"
    ]
    """<p>The S3 bucket that contains the input file.</p>"""
    input_file_key: NotRequired["capo_iot.types.registry_s3_key_name.RegistryS3KeyName"]
    """<p>The input file key.</p>"""
    role_arn: NotRequired["capo_iot.types.role_arn.RoleArn"]
    """<p>The role ARN that grants access to the input file bucket.</p>"""
    status: NotRequired["capo_iot.types.status.Status"]
    """<p>The status of the bulk thing provisioning task.</p>"""
    message: NotRequired["capo_iot.types.error_message.ErrorMessage"]
    """<p>The message.</p>"""
    success_count: "capo_iot.types.count.Count"
    """<p>The number of things successfully provisioned.</p>"""
    failure_count: "capo_iot.types.count.Count"
    """<p>The number of things that failed to be provisioned.</p>"""
    percentage_progress: "capo_iot.types.percentage.Percentage"
    """<p>The progress of the bulk provisioning task expressed as a percentage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThingRegistrationTaskResponse) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "creation_date" in value:
        import capo_iot.types.creation_date

        out["creationDate"] = capo_iot.types.creation_date.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import capo_iot.types.last_modified_date

        out["lastModifiedDate"] = capo_iot.types.last_modified_date.serialize_json(
            value["last_modified_date"]
        )
    if "template_body" in value:
        out["templateBody"] = value["template_body"]
    if "input_file_bucket" in value:
        out["inputFileBucket"] = value["input_file_bucket"]
    if "input_file_key" in value:
        out["inputFileKey"] = value["input_file_key"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "status" in value:
        import capo_iot.types.status

        out["status"] = capo_iot.types.status.serialize_json(value["status"])
    if "message" in value:
        out["message"] = value["message"]
    out["successCount"] = value.get("success_count", 0)
    out["failureCount"] = value.get("failure_count", 0)
    out["percentageProgress"] = value.get("percentage_progress", 0)
    return out


def deserialize_json(data: dict) -> DescribeThingRegistrationTaskResponse:
    out: DescribeThingRegistrationTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "creationDate" in data:
        import capo_iot.types.creation_date

        out["creation_date"] = capo_iot.types.creation_date.deserialize_json(
            data["creationDate"]
        )
    if "lastModifiedDate" in data:
        import capo_iot.types.last_modified_date

        out["last_modified_date"] = capo_iot.types.last_modified_date.deserialize_json(
            data["lastModifiedDate"]
        )
    if "templateBody" in data:
        out["template_body"] = data["templateBody"]
    if "inputFileBucket" in data:
        out["input_file_bucket"] = data["inputFileBucket"]
    if "inputFileKey" in data:
        out["input_file_key"] = data["inputFileKey"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "status" in data:
        import capo_iot.types.status

        out["status"] = capo_iot.types.status.deserialize_json(data["status"])
    if "message" in data:
        out["message"] = data["message"]
    if "successCount" in data:
        out["success_count"] = data["successCount"]
    else:
        out["success_count"] = 0
    if "failureCount" in data:
        out["failure_count"] = data["failureCount"]
    else:
        out["failure_count"] = 0
    if "percentageProgress" in data:
        out["percentage_progress"] = data["percentageProgress"]
    else:
        out["percentage_progress"] = 0
    return out
