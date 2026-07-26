"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteServiceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.service_profile_id


class DeleteServiceProfileRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.service_profile_id.ServiceProfileId"
    """<p>The ID of the resource to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteServiceProfileRequest:
    out: DeleteServiceProfileRequest = {}  # type: ignore[typeddict-item]
    return out
