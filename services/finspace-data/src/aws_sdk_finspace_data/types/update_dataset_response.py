"""Generated from Smithy shape ``com.amazonaws.finspacedata#UpdateDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.dataset_id


class UpdateDatasetResponse(TypedDict, closed=True):
    dataset_id: NotRequired["aws_sdk_finspace_data.types.dataset_id.DatasetId"]
    """<p>The unique identifier for updated Dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_id" in value:
        out["datasetId"] = value["dataset_id"]
    return out


def deserialize_json(data: dict) -> UpdateDatasetResponse:
    out: UpdateDatasetResponse = {}  # type: ignore[typeddict-item]
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    return out
