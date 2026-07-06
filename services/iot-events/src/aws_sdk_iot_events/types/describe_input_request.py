"""Generated from Smithy shape ``com.amazonaws.iotevents#DescribeInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.input_name


class DescribeInputRequest(TypedDict, closed=True):
    input_name: "aws_sdk_iot_events.types.input_name.InputName"
    """<p>The name of the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeInputRequest:
    out: DescribeInputRequest = {}  # type: ignore[typeddict-item]
    return out
