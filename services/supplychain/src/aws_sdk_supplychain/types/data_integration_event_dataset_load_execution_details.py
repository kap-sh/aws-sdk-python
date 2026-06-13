"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationEventDatasetLoadExecutionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_event_dataset_load_status


class DataIntegrationEventDatasetLoadExecutionDetails(TypedDict):
    status: "aws_sdk_supplychain.types.data_integration_event_dataset_load_status.DataIntegrationEventDatasetLoadStatus"
    """<p>The event load execution status to target dataset.</p>"""
    message: NotRequired["str"]
    """<p>The failure message (if any) of failed event load execution to dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationEventDatasetLoadExecutionDetails) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_integration_event_dataset_load_status

    out["status"] = (
        aws_sdk_supplychain.types.data_integration_event_dataset_load_status.serialize_json(
            value["status"]
        )
    )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DataIntegrationEventDatasetLoadExecutionDetails:
    out: DataIntegrationEventDatasetLoadExecutionDetails = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_supplychain.types.data_integration_event_dataset_load_status

        out["status"] = (
            aws_sdk_supplychain.types.data_integration_event_dataset_load_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "DataIntegrationEventDatasetLoadExecutionDetails.status required"
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
