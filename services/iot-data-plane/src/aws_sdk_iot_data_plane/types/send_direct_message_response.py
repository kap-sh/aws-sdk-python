"""Generated from Smithy shape ``com.amazonaws.iotdataplane#SendDirectMessageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.response_message
    import aws_sdk_iot_data_plane.types.trace_id


class SendDirectMessageResponse(TypedDict):
    message: NotRequired[
        "aws_sdk_iot_data_plane.types.response_message.ResponseMessage"
    ]
    """<p>The status message indicating the result of the operation.</p>"""
    trace_id: NotRequired["aws_sdk_iot_data_plane.types.trace_id.TraceId"]
    """<p>A unique identifier for the request. Include this value when contacting Amazon Web Services Support for troubleshooting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendDirectMessageResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "trace_id" in value:
        out["traceId"] = value["trace_id"]
    return out


def deserialize_json(data: dict) -> SendDirectMessageResponse:
    out: SendDirectMessageResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "traceId" in data:
        out["trace_id"] = data["traceId"]
    return out
