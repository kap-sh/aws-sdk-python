"""Generated from Smithy shape ``com.amazonaws.iotevents#DescribeInputResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.input


class DescribeInputResponse(TypedDict):
    input: NotRequired["aws_sdk_iot_events.types.input.Input"]
    """<p>Information about the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInputResponse) -> dict:
    out: dict = {}
    if "input" in value:
        import aws_sdk_iot_events.types.input

        out["input"] = aws_sdk_iot_events.types.input.serialize_json(value["input"])
    return out


def deserialize_json(data: dict) -> DescribeInputResponse:
    out: DescribeInputResponse = {}  # type: ignore[typeddict-item]
    if "input" in data:
        import aws_sdk_iot_events.types.input

        out["input"] = aws_sdk_iot_events.types.input.deserialize_json(data["input"])
    return out
