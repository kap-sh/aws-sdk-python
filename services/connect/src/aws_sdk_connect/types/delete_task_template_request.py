"""Generated from Smithy shape ``com.amazonaws.connect#DeleteTaskTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.task_template_id


class DeleteTaskTemplateRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    task_template_id: "aws_sdk_connect.types.task_template_id.TaskTemplateId"
    """<p>A unique identifier for the task template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTaskTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTaskTemplateRequest:
    out: DeleteTaskTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
