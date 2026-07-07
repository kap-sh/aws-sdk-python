"""Generated from Smithy shape ``com.amazonaws.wickr#BatchDeviceErrorResponseItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string


class BatchDeviceErrorResponseItem(TypedDict, closed=True):
    field: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The field that caused the error.</p>"""
    reason: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A description of why the device operation failed.</p>"""
    app_id: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The application ID of the device that failed to be processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeviceErrorResponseItem) -> dict:
    out: dict = {}
    if "field" in value:
        out["field"] = value["field"]
    if "reason" in value:
        out["reason"] = value["reason"]
    out["appId"] = value["app_id"]
    return out


def deserialize_json(data: dict) -> BatchDeviceErrorResponseItem:
    out: BatchDeviceErrorResponseItem = {}  # type: ignore[typeddict-item]
    if "field" in data:
        out["field"] = data["field"]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("BatchDeviceErrorResponseItem.app_id required")
    return out
