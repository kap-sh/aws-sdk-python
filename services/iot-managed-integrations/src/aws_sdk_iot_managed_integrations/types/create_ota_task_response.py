"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateOtaTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.ota_description
    import aws_sdk_iot_managed_integrations.types.ota_task_arn
    import aws_sdk_iot_managed_integrations.types.ota_task_id


class CreateOtaTaskResponse(TypedDict, closed=True):
    task_id: NotRequired["aws_sdk_iot_managed_integrations.types.ota_task_id.OtaTaskId"]
    """<p>The identifier of the over-the-air (OTA) task.</p>"""
    task_arn: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_task_arn.OtaTaskArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the over-the-air (OTA) task.</p>"""
    description: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_description.OtaDescription"
    ]
    """<p>A description of the over-the-air (OTA) task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOtaTaskResponse) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateOtaTaskResponse:
    out: CreateOtaTaskResponse = {}  # type: ignore[typeddict-item]
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    if "TaskArn" in data:
        out["task_arn"] = data["TaskArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
