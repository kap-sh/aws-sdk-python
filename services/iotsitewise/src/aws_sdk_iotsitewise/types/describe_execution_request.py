"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class DescribeExecutionRequest(TypedDict, closed=True):
    execution_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeExecutionRequest:
    out: DescribeExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
