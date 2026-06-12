"""Generated from Smithy shape ``com.amazonaws.wickr#BatchDeviceSuccessResponseItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string


class BatchDeviceSuccessResponseItem(TypedDict):
    app_id: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The application ID of the device that was successfully processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeviceSuccessResponseItem) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    return out


def deserialize_json(data: dict) -> BatchDeviceSuccessResponseItem:
    out: BatchDeviceSuccessResponseItem = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("BatchDeviceSuccessResponseItem.app_id required")
    return out
