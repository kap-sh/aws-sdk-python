"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeleteOtaTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.ota_task_id


class DeleteOtaTaskRequest(TypedDict):
    identifier: "aws_sdk_iot_managed_integrations.types.ota_task_id.OtaTaskId"
    """<p>The identifier of the over-the-air (OTA) task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOtaTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteOtaTaskRequest:
    out: DeleteOtaTaskRequest = {}  # type: ignore[typeddict-item]
    return out
