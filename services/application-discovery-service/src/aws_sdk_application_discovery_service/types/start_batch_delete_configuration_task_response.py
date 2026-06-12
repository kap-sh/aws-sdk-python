"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StartBatchDeleteConfigurationTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.uuid


class StartBatchDeleteConfigurationTaskResponse(TypedDict):
    task_id: NotRequired["aws_sdk_application_discovery_service.types.uuid.UUID"]
    """<p> The unique identifier associated with the newly started deletion task. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartBatchDeleteConfigurationTaskResponse) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartBatchDeleteConfigurationTaskResponse:
    out: StartBatchDeleteConfigurationTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    return out
