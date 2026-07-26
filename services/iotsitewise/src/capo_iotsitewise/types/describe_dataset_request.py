"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class DescribeDatasetRequest(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDatasetRequest:
    out: DescribeDatasetRequest = {}  # type: ignore[typeddict-item]
    return out
