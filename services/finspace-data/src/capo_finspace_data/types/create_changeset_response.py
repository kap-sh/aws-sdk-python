"""Generated from Smithy shape ``com.amazonaws.finspacedata#CreateChangesetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.changeset_id
    import capo_finspace_data.types.dataset_id


class CreateChangesetResponse(TypedDict, closed=True):
    dataset_id: NotRequired["capo_finspace_data.types.dataset_id.DatasetId"]
    """<p>The unique identifier for the FinSpace Dataset where the Changeset is created.</p>"""
    changeset_id: NotRequired["capo_finspace_data.types.changeset_id.ChangesetId"]
    """<p>The unique identifier of the Changeset that is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChangesetResponse) -> dict:
    out: dict = {}
    if "dataset_id" in value:
        out["datasetId"] = value["dataset_id"]
    if "changeset_id" in value:
        out["changesetId"] = value["changeset_id"]
    return out


def deserialize_json(data: dict) -> CreateChangesetResponse:
    out: CreateChangesetResponse = {}  # type: ignore[typeddict-item]
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    if "changesetId" in data:
        out["changeset_id"] = data["changesetId"]
    return out
