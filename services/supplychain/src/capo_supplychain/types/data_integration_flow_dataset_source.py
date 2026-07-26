"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowDatasetSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_dataset_arn


class DataIntegrationFlowDatasetSource(TypedDict, closed=True):
    dataset_identifier: (
        "capo_supplychain.types.data_integration_dataset_arn.DataIntegrationDatasetArn"
    )
    """<p>The ARN of the dataset source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowDatasetSource) -> dict:
    out: dict = {}
    out["datasetIdentifier"] = value["dataset_identifier"]
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowDatasetSource:
    out: DataIntegrationFlowDatasetSource = {}  # type: ignore[typeddict-item]
    if "datasetIdentifier" in data:
        out["dataset_identifier"] = data["datasetIdentifier"]
    else:
        raise DeserializationError(
            "DataIntegrationFlowDatasetSource.dataset_identifier required"
        )
    return out
