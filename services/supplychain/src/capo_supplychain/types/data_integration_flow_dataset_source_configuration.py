"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowDatasetSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_dataset_options
    import capo_supplychain.types.dataset_identifier


class DataIntegrationFlowDatasetSourceConfiguration(TypedDict, closed=True):
    dataset_identifier: "capo_supplychain.types.dataset_identifier.DatasetIdentifier"
    """<p>The ARN of the dataset.</p>"""
    options: NotRequired[
        "capo_supplychain.types.data_integration_flow_dataset_options.DataIntegrationFlowDatasetOptions"
    ]
    """<p>The dataset DataIntegrationFlow source options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowDatasetSourceConfiguration) -> dict:
    out: dict = {}
    out["datasetIdentifier"] = value["dataset_identifier"]
    if "options" in value:
        import capo_supplychain.types.data_integration_flow_dataset_options

        out["options"] = (
            capo_supplychain.types.data_integration_flow_dataset_options.serialize_json(
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
        import capo_supplychain.types.data_integration_flow_dataset_options

        out["options"] = (
            capo_supplychain.types.data_integration_flow_dataset_options.deserialize_json(
                data["options"]
            )
        )
    return out
