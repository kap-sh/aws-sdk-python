"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.dataset_name


class DescribeDatasetRequest(TypedDict, closed=True):
    name: "capo_databrew.types.dataset_name.DatasetName"
    """<p>The name of the dataset to be described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDatasetRequest:
    out: DescribeDatasetRequest = {}  # type: ignore[typeddict-item]
    return out
