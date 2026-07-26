"""Generated from Smithy shape ``com.amazonaws.route53profiles#DisassociateProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53profiles.types.resource_id


class DisassociateProfileRequest(TypedDict, closed=True):
    profile_id: "capo_route53profiles.types.resource_id.ResourceId"
    """<p> ID of the Profile. </p>"""
    resource_id: "capo_route53profiles.types.resource_id.ResourceId"
    """<p> The ID of the VPC. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateProfileRequest:
    out: DisassociateProfileRequest = {}  # type: ignore[typeddict-item]
    return out
