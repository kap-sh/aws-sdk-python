"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class DescribeActionRequest(TypedDict, closed=True):
    action_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeActionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeActionRequest:
    out: DescribeActionRequest = {}  # type: ignore[typeddict-item]
    return out
