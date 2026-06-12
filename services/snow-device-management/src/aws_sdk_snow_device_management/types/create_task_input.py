"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#CreateTaskInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_snow_device_management.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.command
    import aws_sdk_snow_device_management.types.idempotency_token
    import aws_sdk_snow_device_management.types.tag_map
    import aws_sdk_snow_device_management.types.target_list
    import aws_sdk_snow_device_management.types.task_description_string

class CreateTaskInput(TypedDict):
    targets: "aws_sdk_snow_device_management.types.target_list.TargetList"
    """<p>A list of managed device IDs.</p>"""
    command: "aws_sdk_snow_device_management.types.command.Command"
    """<p>The task to be performed. Only one task is executed on a device at a time.</p>"""
    description: NotRequired["aws_sdk_snow_device_management.types.task_description_string.TaskDescriptionString"]
    """<p>A description of the task and its targets.</p>"""
    tags: NotRequired["aws_sdk_snow_device_management.types.tag_map.TagMap"]
    """<p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment. </p>"""
    client_token: NotRequired["aws_sdk_snow_device_management.types.idempotency_token.IdempotencyToken"]
    """<p>A token ensuring that the action is called only once with the specified details.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateTaskInput) -> dict:
    out: dict = {}
    import aws_sdk_snow_device_management.types.target_list
    out["targets"] = aws_sdk_snow_device_management.types.target_list.serialize_json(value["targets"])
    import aws_sdk_snow_device_management.types.command
    out["command"] = aws_sdk_snow_device_management.types.command.serialize_json(value["command"])
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_snow_device_management.types.tag_map
        out["tags"] = aws_sdk_snow_device_management.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateTaskInput:
    out: CreateTaskInput = {}  # type: ignore[typeddict-item]
    if "targets" in data:
        import aws_sdk_snow_device_management.types.target_list
        out["targets"] = aws_sdk_snow_device_management.types.target_list.deserialize_json(data["targets"])
    else:
        raise DeserializationError("CreateTaskInput.targets required")
    if "command" in data:
        import aws_sdk_snow_device_management.types.command
        out["command"] = aws_sdk_snow_device_management.types.command.deserialize_json(data["command"])
    else:
        raise DeserializationError("CreateTaskInput.command required")
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_snow_device_management.types.tag_map
        out["tags"] = aws_sdk_snow_device_management.types.tag_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out