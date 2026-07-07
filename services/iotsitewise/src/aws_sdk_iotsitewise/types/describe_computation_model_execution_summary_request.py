"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeComputationModelExecutionSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.resolve_to_resource_type


class DescribeComputationModelExecutionSummaryRequest(TypedDict, closed=True):
    computation_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the computation model.</p>"""
    resolve_to_resource_type: NotRequired[
        "aws_sdk_iotsitewise.types.resolve_to_resource_type.ResolveToResourceType"
    ]
    """<p>The type of the resolved resource.</p>"""
    resolve_to_resource_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the resolved resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeComputationModelExecutionSummaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeComputationModelExecutionSummaryRequest:
    out: DescribeComputationModelExecutionSummaryRequest = {}  # type: ignore[typeddict-item]
    return out
