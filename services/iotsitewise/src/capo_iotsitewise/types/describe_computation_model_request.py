"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeComputationModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.computation_model_version_filter
    import capo_iotsitewise.types.id


class DescribeComputationModelRequest(TypedDict, closed=True):
    computation_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the computation model.</p>"""
    computation_model_version: NotRequired[
        "capo_iotsitewise.types.computation_model_version_filter.ComputationModelVersionFilter"
    ]
    """<p>The version of the computation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeComputationModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeComputationModelRequest:
    out: DescribeComputationModelRequest = {}  # type: ignore[typeddict-item]
    return out
