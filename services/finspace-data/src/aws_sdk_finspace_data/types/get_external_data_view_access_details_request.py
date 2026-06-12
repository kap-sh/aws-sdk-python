"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetExternalDataViewAccessDetailsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.data_view_id
    import aws_sdk_finspace_data.types.dataset_id


class GetExternalDataViewAccessDetailsRequest(TypedDict):
    data_view_id: "aws_sdk_finspace_data.types.data_view_id.DataViewId"
    """<p>The unique identifier for the Dataview that you want to access.</p>"""
    dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId"
    """<p>The unique identifier for the Dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExternalDataViewAccessDetailsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExternalDataViewAccessDetailsRequest:
    out: GetExternalDataViewAccessDetailsRequest = {}  # type: ignore[typeddict-item]
    return out
