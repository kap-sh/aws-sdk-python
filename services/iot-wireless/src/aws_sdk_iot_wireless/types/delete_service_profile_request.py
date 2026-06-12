"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteServiceProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.service_profile_id


class DeleteServiceProfileRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.service_profile_id.ServiceProfileId"
    """<p>The ID of the resource to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteServiceProfileRequest:
    out: DeleteServiceProfileRequest = {}  # type: ignore[typeddict-item]
    return out
