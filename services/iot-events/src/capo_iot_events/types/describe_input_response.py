"""Generated from Smithy shape ``com.amazonaws.iotevents#DescribeInputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.input


class DescribeInputResponse(TypedDict, closed=True):
    input: NotRequired["capo_iot_events.types.input.Input"]
    """<p>Information about the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInputResponse) -> dict:
    out: dict = {}
    if "input" in value:
        import capo_iot_events.types.input

        out["input"] = capo_iot_events.types.input.serialize_json(value["input"])
    return out


def deserialize_json(data: dict) -> DescribeInputResponse:
    out: DescribeInputResponse = {}  # type: ignore[typeddict-item]
    if "input" in data:
        import capo_iot_events.types.input

        out["input"] = capo_iot_events.types.input.deserialize_json(data["input"])
    return out
