"""Generated from Smithy shape ``com.amazonaws.route53profiles#DeleteProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53profiles.types.resource_id


class DeleteProfileRequest(TypedDict, closed=True):
    profile_id: "capo_route53profiles.types.resource_id.ResourceId"
    """<p> The ID of the Profile that you want to delete. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProfileRequest:
    out: DeleteProfileRequest = {}  # type: ignore[typeddict-item]
    return out
