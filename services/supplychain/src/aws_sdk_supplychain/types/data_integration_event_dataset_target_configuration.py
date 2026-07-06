"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationEventDatasetTargetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_dataset_arn
    import aws_sdk_supplychain.types.data_integration_event_dataset_operation_type


class DataIntegrationEventDatasetTargetConfiguration(TypedDict, closed=True):
    dataset_identifier: "aws_sdk_supplychain.types.data_integration_dataset_arn.DataIntegrationDatasetArn"
    """<p>The datalake dataset ARN identifier.</p>"""
    operation_type: "aws_sdk_supplychain.types.data_integration_event_dataset_operation_type.DataIntegrationEventDatasetOperationType"
    """<p>The target dataset load operation type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationEventDatasetTargetConfiguration) -> dict:
    out: dict = {}
    out["datasetIdentifier"] = value["dataset_identifier"]
    import aws_sdk_supplychain.types.data_integration_event_dataset_operation_type

    out["operationType"] = (
        aws_sdk_supplychain.types.data_integration_event_dataset_operation_type.serialize_json(
            value["operation_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataIntegrationEventDatasetTargetConfiguration:
    out: DataIntegrationEventDatasetTargetConfiguration = {}  # type: ignore[typeddict-item]
    if "datasetIdentifier" in data:
        out["dataset_identifier"] = data["datasetIdentifier"]
    else:
        raise DeserializationError(
            "DataIntegrationEventDatasetTargetConfiguration.dataset_identifier required"
        )
    if "operationType" in data:
        import aws_sdk_supplychain.types.data_integration_event_dataset_operation_type

        out["operation_type"] = (
            aws_sdk_supplychain.types.data_integration_event_dataset_operation_type.deserialize_json(
                data["operationType"]
            )
        )
    else:
        raise DeserializationError(
            "DataIntegrationEventDatasetTargetConfiguration.operation_type required"
        )
    return out
