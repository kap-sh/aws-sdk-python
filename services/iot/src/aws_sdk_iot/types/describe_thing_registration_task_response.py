"""Generated from Smithy shape ``com.amazonaws.iot#DescribeThingRegistrationTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.count
    import aws_sdk_iot.types.creation_date
    import aws_sdk_iot.types.error_message
    import aws_sdk_iot.types.last_modified_date
    import aws_sdk_iot.types.percentage
    import aws_sdk_iot.types.registry_s3_bucket_name
    import aws_sdk_iot.types.registry_s3_key_name
    import aws_sdk_iot.types.role_arn
    import aws_sdk_iot.types.status
    import aws_sdk_iot.types.task_id
    import aws_sdk_iot.types.template_body


class DescribeThingRegistrationTaskResponse(TypedDict):
    task_id: NotRequired["aws_sdk_iot.types.task_id.TaskId"]
    """<p>The task ID.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.creation_date.CreationDate"]
    """<p>The task creation date.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_iot.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date when the task was last modified.</p>"""
    template_body: NotRequired["aws_sdk_iot.types.template_body.TemplateBody"]
    """<p>The task's template.</p>"""
    input_file_bucket: NotRequired[
        "aws_sdk_iot.types.registry_s3_bucket_name.RegistryS3BucketName"
    ]
    """<p>The S3 bucket that contains the input file.</p>"""
    input_file_key: NotRequired[
        "aws_sdk_iot.types.registry_s3_key_name.RegistryS3KeyName"
    ]
    """<p>The input file key.</p>"""
    role_arn: NotRequired["aws_sdk_iot.types.role_arn.RoleArn"]
    """<p>The role ARN that grants access to the input file bucket.</p>"""
    status: NotRequired["aws_sdk_iot.types.status.Status"]
    """<p>The status of the bulk thing provisioning task.</p>"""
    message: NotRequired["aws_sdk_iot.types.error_message.ErrorMessage"]
    """<p>The message.</p>"""
    success_count: "aws_sdk_iot.types.count.Count"
    """<p>The number of things successfully provisioned.</p>"""
    failure_count: "aws_sdk_iot.types.count.Count"
    """<p>The number of things that failed to be provisioned.</p>"""
    percentage_progress: "aws_sdk_iot.types.percentage.Percentage"
    """<p>The progress of the bulk provisioning task expressed as a percentage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThingRegistrationTaskResponse) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "creation_date" in value:
        import aws_sdk_iot.types.creation_date

        out["creationDate"] = aws_sdk_iot.types.creation_date.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import aws_sdk_iot.types.last_modified_date

        out["lastModifiedDate"] = aws_sdk_iot.types.last_modified_date.serialize_json(
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
        import aws_sdk_iot.types.status

        out["status"] = aws_sdk_iot.types.status.serialize_json(value["status"])
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
        import aws_sdk_iot.types.creation_date

        out["creation_date"] = aws_sdk_iot.types.creation_date.deserialize_json(
            data["creationDate"]
        )
    if "lastModifiedDate" in data:
        import aws_sdk_iot.types.last_modified_date

        out["last_modified_date"] = (
            aws_sdk_iot.types.last_modified_date.deserialize_json(
                data["lastModifiedDate"]
            )
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
        import aws_sdk_iot.types.status

        out["status"] = aws_sdk_iot.types.status.deserialize_json(data["status"])
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
