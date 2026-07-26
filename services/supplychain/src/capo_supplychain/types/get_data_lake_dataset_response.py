"""Generated from Smithy shape ``com.amazonaws.supplychain#GetDataLakeDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset


class GetDataLakeDatasetResponse(TypedDict, closed=True):
    dataset: "capo_supplychain.types.data_lake_dataset.DataLakeDataset"
    """<p>The fetched dataset details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataLakeDatasetResponse) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_lake_dataset

    out["dataset"] = capo_supplychain.types.data_lake_dataset.serialize_json(
        value["dataset"]
    )
    return out


def deserialize_json(data: dict) -> GetDataLakeDatasetResponse:
    out: GetDataLakeDatasetResponse = {}  # type: ignore[typeddict-item]
    if "dataset" in data:
        import capo_supplychain.types.data_lake_dataset

        out["dataset"] = capo_supplychain.types.data_lake_dataset.deserialize_json(
            data["dataset"]
        )
    else:
        raise DeserializationError("GetDataLakeDatasetResponse.dataset required")
    return out
