"""Generated from Smithy shape ``com.amazonaws.supplychain#UpdateDataLakeDatasetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_lake_dataset


class UpdateDataLakeDatasetResponse(TypedDict):
    dataset: "aws_sdk_supplychain.types.data_lake_dataset.DataLakeDataset"
    """<p>The updated dataset details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataLakeDatasetResponse) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_lake_dataset

    out["dataset"] = aws_sdk_supplychain.types.data_lake_dataset.serialize_json(
        value["dataset"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataLakeDatasetResponse:
    out: UpdateDataLakeDatasetResponse = {}  # type: ignore[typeddict-item]
    if "dataset" in data:
        import aws_sdk_supplychain.types.data_lake_dataset

        out["dataset"] = aws_sdk_supplychain.types.data_lake_dataset.deserialize_json(
            data["dataset"]
        )
    else:
        raise DeserializationError("UpdateDataLakeDatasetResponse.dataset required")
    return out
