"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetDataViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.data_view_id
    import aws_sdk_finspace_data.types.dataset_id


class GetDataViewRequest(TypedDict, closed=True):
    data_view_id: "aws_sdk_finspace_data.types.data_view_id.DataViewId"
    """<p>The unique identifier for the Dataview.</p>"""
    dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId"
    """<p>The unique identifier for the Dataset used in the Dataview.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataViewRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataViewRequest:
    out: GetDataViewRequest = {}  # type: ignore[typeddict-item]
    return out
