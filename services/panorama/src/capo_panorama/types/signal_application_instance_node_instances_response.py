"""Generated from Smithy shape ``com.amazonaws.panorama#SignalApplicationInstanceNodeInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.application_instance_id


class SignalApplicationInstanceNodeInstancesResponse(TypedDict, closed=True):
    application_instance_id: (
        "capo_panorama.types.application_instance_id.ApplicationInstanceId"
    )
    """<p>An application instance ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SignalApplicationInstanceNodeInstancesResponse) -> dict:
    out: dict = {}
    out["ApplicationInstanceId"] = value["application_instance_id"]
    return out


def deserialize_json(data: dict) -> SignalApplicationInstanceNodeInstancesResponse:
    out: SignalApplicationInstanceNodeInstancesResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationInstanceId" in data:
        out["application_instance_id"] = data["ApplicationInstanceId"]
    else:
        raise DeserializationError(
            "SignalApplicationInstanceNodeInstancesResponse.application_instance_id required"
        )
    return out
