"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetOtaTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.ota_task_id


class GetOtaTaskRequest(TypedDict, closed=True):
    identifier: "aws_sdk_iot_managed_integrations.types.ota_task_id.OtaTaskId"
    """<p>The over-the-air (OTA) task id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOtaTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOtaTaskRequest:
    out: GetOtaTaskRequest = {}  # type: ignore[typeddict-item]
    return out
