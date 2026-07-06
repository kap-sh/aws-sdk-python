"""Generated from Smithy shape ``com.amazonaws.finspacedata#CreateDataViewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.data_view_id
    import aws_sdk_finspace_data.types.dataset_id


class CreateDataViewResponse(TypedDict, closed=True):
    dataset_id: NotRequired["aws_sdk_finspace_data.types.dataset_id.DatasetId"]
    """<p>The unique identifier of the Dataset used for the Dataview.</p>"""
    data_view_id: NotRequired["aws_sdk_finspace_data.types.data_view_id.DataViewId"]
    """<p>The unique identifier for the created Dataview.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataViewResponse) -> dict:
    out: dict = {}
    if "dataset_id" in value:
        out["datasetId"] = value["dataset_id"]
    if "data_view_id" in value:
        out["dataViewId"] = value["data_view_id"]
    return out


def deserialize_json(data: dict) -> CreateDataViewResponse:
    out: CreateDataViewResponse = {}  # type: ignore[typeddict-item]
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    if "dataViewId" in data:
        out["data_view_id"] = data["dataViewId"]
    return out
