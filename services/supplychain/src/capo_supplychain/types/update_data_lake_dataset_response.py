"""Generated from Smithy shape ``com.amazonaws.supplychain#UpdateDataLakeDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset


class UpdateDataLakeDatasetResponse(TypedDict, closed=True):
    dataset: "capo_supplychain.types.data_lake_dataset.DataLakeDataset"
    """<p>The updated dataset details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataLakeDatasetResponse) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_lake_dataset

    out["dataset"] = capo_supplychain.types.data_lake_dataset.serialize_json(
        value["dataset"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataLakeDatasetResponse:
    out: UpdateDataLakeDatasetResponse = {}  # type: ignore[typeddict-item]
    if "dataset" in data:
        import capo_supplychain.types.data_lake_dataset

        out["dataset"] = capo_supplychain.types.data_lake_dataset.deserialize_json(
            data["dataset"]
        )
    else:
        raise DeserializationError("UpdateDataLakeDatasetResponse.dataset required")
    return out
