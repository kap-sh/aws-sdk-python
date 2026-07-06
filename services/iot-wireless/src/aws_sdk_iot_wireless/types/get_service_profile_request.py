"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetServiceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.service_profile_id


class GetServiceProfileRequest(TypedDict, closed=True):
    id: "aws_sdk_iot_wireless.types.service_profile_id.ServiceProfileId"
    """<p>The ID of the resource to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServiceProfileRequest:
    out: GetServiceProfileRequest = {}  # type: ignore[typeddict-item]
    return out
