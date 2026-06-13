"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ScalarProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.uuid


class ScalarProfileRequest(TypedDict):
    profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid"
    """<p>The unique identifier of the profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScalarProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ScalarProfileRequest:
    out: ScalarProfileRequest = {}  # type: ignore[typeddict-item]
    return out
