"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateInfoV2``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.task_template_name


class TaskTemplateInfoV2(TypedDict):
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the task template used to create this contact.</p>"""
    name: NotRequired["aws_sdk_connect.types.task_template_name.TaskTemplateName"]
    """<p>The name of the task template used to create this contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskTemplateInfoV2) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> TaskTemplateInfoV2:
    out: TaskTemplateInfoV2 = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
