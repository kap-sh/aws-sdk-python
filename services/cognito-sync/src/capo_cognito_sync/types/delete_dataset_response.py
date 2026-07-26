"""Generated from Smithy shape ``com.amazonaws.cognitosync#DeleteDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.dataset


class DeleteDatasetResponse(TypedDict, closed=True):
    dataset: NotRequired["capo_cognito_sync.types.dataset.Dataset"]
    """A collection of data for an identity pool. An identity pool can have multiple datasets. A dataset is per identity and can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don't exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatasetResponse) -> dict:
    out: dict = {}
    if "dataset" in value:
        import capo_cognito_sync.types.dataset

        out["Dataset"] = capo_cognito_sync.types.dataset.serialize_json(
            value["dataset"]
        )
    return out


def deserialize_json(data: dict) -> DeleteDatasetResponse:
    out: DeleteDatasetResponse = {}  # type: ignore[typeddict-item]
    if "Dataset" in data:
        import capo_cognito_sync.types.dataset

        out["dataset"] = capo_cognito_sync.types.dataset.deserialize_json(
            data["Dataset"]
        )
    return out
