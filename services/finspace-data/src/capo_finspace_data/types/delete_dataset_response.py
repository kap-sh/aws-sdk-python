"""Generated from Smithy shape ``com.amazonaws.finspacedata#DeleteDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.dataset_id


class DeleteDatasetResponse(TypedDict, closed=True):
    dataset_id: NotRequired["capo_finspace_data.types.dataset_id.DatasetId"]
    """<p>The unique identifier for the deleted Dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_id" in value:
        out["datasetId"] = value["dataset_id"]
    return out


def deserialize_json(data: dict) -> DeleteDatasetResponse:
    out: DeleteDatasetResponse = {}  # type: ignore[typeddict-item]
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    return out
