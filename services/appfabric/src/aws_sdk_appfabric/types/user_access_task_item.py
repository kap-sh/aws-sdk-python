"""Generated from Smithy shape ``com.amazonaws.appfabric#UserAccessTaskItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.string255
    import aws_sdk_appfabric.types.task_error
    import aws_sdk_appfabric.types.tenant_identifier
    import aws_sdk_appfabric.types.uuid


class UserAccessTaskItem(TypedDict):
    app: "aws_sdk_appfabric.types.string255.String255"
    """<p>The name of the application.</p>"""
    tenant_id: "aws_sdk_appfabric.types.tenant_identifier.TenantIdentifier"
    """<p>The ID of the application tenant.</p>"""
    task_id: NotRequired["aws_sdk_appfabric.types.uuid.UUID"]
    """<p>The unique ID of the task.</p>"""
    error: NotRequired["aws_sdk_appfabric.types.task_error.TaskError"]
    """<p>Error from the task, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserAccessTaskItem) -> dict:
    out: dict = {}
    out["app"] = value["app"]
    out["tenantId"] = value["tenant_id"]
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "error" in value:
        import aws_sdk_appfabric.types.task_error

        out["error"] = aws_sdk_appfabric.types.task_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> UserAccessTaskItem:
    out: UserAccessTaskItem = {}  # type: ignore[typeddict-item]
    if "app" in data:
        out["app"] = data["app"]
    else:
        raise DeserializationError("UserAccessTaskItem.app required")
    if "tenantId" in data:
        out["tenant_id"] = data["tenantId"]
    else:
        raise DeserializationError("UserAccessTaskItem.tenant_id required")
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "error" in data:
        import aws_sdk_appfabric.types.task_error

        out["error"] = aws_sdk_appfabric.types.task_error.deserialize_json(
            data["error"]
        )
    return out
