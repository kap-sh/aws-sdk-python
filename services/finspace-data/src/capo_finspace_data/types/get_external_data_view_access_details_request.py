"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetExternalDataViewAccessDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.data_view_id
    import capo_finspace_data.types.dataset_id


class GetExternalDataViewAccessDetailsRequest(TypedDict, closed=True):
    data_view_id: "capo_finspace_data.types.data_view_id.DataViewId"
    """<p>The unique identifier for the Dataview that you want to access.</p>"""
    dataset_id: "capo_finspace_data.types.dataset_id.DatasetId"
    """<p>The unique identifier for the Dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExternalDataViewAccessDetailsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExternalDataViewAccessDetailsRequest:
    out: GetExternalDataViewAccessDetailsRequest = {}  # type: ignore[typeddict-item]
    return out
