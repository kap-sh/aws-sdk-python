"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetDatasetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.string_value_length1to255


class GetDatasetRequest(TypedDict):
    dataset_id: (
        "aws_sdk_finspace_data.types.string_value_length1to255.StringValueLength1to255"
    )
    """<p>The unique identifier for a Dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDatasetRequest:
    out: GetDatasetRequest = {}  # type: ignore[typeddict-item]
    return out
