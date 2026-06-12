"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeBatchDeleteConfigurationTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.uuid


class DescribeBatchDeleteConfigurationTaskRequest(TypedDict):
    task_id: "aws_sdk_application_discovery_service.types.uuid.UUID"
    """<p> The ID of the task to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBatchDeleteConfigurationTaskRequest) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBatchDeleteConfigurationTaskRequest:
    out: DescribeBatchDeleteConfigurationTaskRequest = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError(
            "DescribeBatchDeleteConfigurationTaskRequest.task_id required"
        )
    return out
