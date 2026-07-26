"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.dataset_name


class DeleteDatasetRequest(TypedDict, closed=True):
    name: "capo_databrew.types.dataset_name.DatasetName"
    """<p>The name of the dataset to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDatasetRequest:
    out: DeleteDatasetRequest = {}  # type: ignore[typeddict-item]
    return out
