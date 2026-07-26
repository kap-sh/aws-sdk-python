"""Generated from Smithy shape ``com.amazonaws.panorama#RemoveApplicationInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.application_instance_id


class RemoveApplicationInstanceRequest(TypedDict, closed=True):
    application_instance_id: (
        "capo_panorama.types.application_instance_id.ApplicationInstanceId"
    )
    """<p>An application instance ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveApplicationInstanceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveApplicationInstanceRequest:
    out: RemoveApplicationInstanceRequest = {}  # type: ignore[typeddict-item]
    return out
