"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DescribeInputRequest(TypedDict, closed=True):
    input_id: "aws_sdk_medialive.types.__string.__string"
    """Unique ID of the input"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeInputRequest:
    out: DescribeInputRequest = {}  # type: ignore[typeddict-item]
    return out
