"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ScalarProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.uuid


class ScalarProfileRequest(TypedDict, closed=True):
    profile_id: "capo_rolesanywhere.types.uuid.Uuid"
    """<p>The unique identifier of the profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScalarProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ScalarProfileRequest:
    out: ScalarProfileRequest = {}  # type: ignore[typeddict-item]
    return out
