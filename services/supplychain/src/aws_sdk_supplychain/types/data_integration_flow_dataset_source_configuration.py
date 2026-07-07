"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowDatasetSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_dataset_options
    import aws_sdk_supplychain.types.dataset_identifier


class DataIntegrationFlowDatasetSourceConfiguration(TypedDict, closed=True):
    dataset_identifier: "aws_sdk_supplychain.types.dataset_identifier.DatasetIdentifier"
    """<p>The ARN of the dataset.</p>"""
    options: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_dataset_options.DataIntegrationFlowDatasetOptions"
    ]
    """<p>The dataset DataIntegrationFlow source options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowDatasetSourceConfiguration) -> dict:
    out: dict = {}
    out["datasetIdentifier"] = value["dataset_identifier"]
    if "options" in value:
        import aws_sdk_supplychain.types.data_integration_flow_dataset_options

        out["options"] = (
            aws_sdk_supplychain.types.data_integration_flow_dataset_options.serialize_json(
                value["options"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowDatasetSourceConfiguration:
    out: DataIntegrationFlowDatasetSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "datasetIdentifier" in data:
        out["dataset_identifier"] = data["datasetIdentifier"]
    else:
        raise DeserializationError(
            "DataIntegrationFlowDatasetSourceConfiguration.dataset_identifier required"
        )
    if "options" in data:
        import aws_sdk_supplychain.types.data_integration_flow_dataset_options

        out["options"] = (
            aws_sdk_supplychain.types.data_integration_flow_dataset_options.deserialize_json(
                data["options"]
            )
        )
    return out
