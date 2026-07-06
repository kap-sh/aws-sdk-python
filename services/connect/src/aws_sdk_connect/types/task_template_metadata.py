"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.task_template_arn
    import aws_sdk_connect.types.task_template_description
    import aws_sdk_connect.types.task_template_id
    import aws_sdk_connect.types.task_template_name
    import aws_sdk_connect.types.task_template_status
    import aws_sdk_connect.types.timestamp


class TaskTemplateMetadata(TypedDict, closed=True):
    id: NotRequired["aws_sdk_connect.types.task_template_id.TaskTemplateId"]
    """<p>A unique identifier for the task template.</p>"""
    arn: NotRequired["aws_sdk_connect.types.task_template_arn.TaskTemplateArn"]
    """<p>The Amazon Resource Name (ARN) of the task template.</p>"""
    name: NotRequired["aws_sdk_connect.types.task_template_name.TaskTemplateName"]
    """<p>The name of the task template.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.task_template_description.TaskTemplateDescription"
    ]
    """<p>The description of the task template.</p>"""
    status: NotRequired["aws_sdk_connect.types.task_template_status.TaskTemplateStatus"]
    """<p>Marks a template as <code>ACTIVE</code> or <code>INACTIVE</code> for a task to refer to it. Tasks can only be created from <code>ACTIVE</code> templates. If a template is marked as <code>INACTIVE</code>, then a task that refers to this template cannot be created.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the task template was last modified.</p>"""
    created_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the task template was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskTemplateMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_connect.types.task_template_status

        out["Status"] = aws_sdk_connect.types.task_template_status.serialize_json(
            value["status"]
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "created_time" in value:
        import aws_sdk_connect.types.timestamp

        out["CreatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["created_time"]
        )
    return out


def deserialize_json(data: dict) -> TaskTemplateMetadata:
    out: TaskTemplateMetadata = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_connect.types.task_template_status

        out["status"] = aws_sdk_connect.types.task_template_status.deserialize_json(
            data["Status"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "CreatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["created_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    return out
