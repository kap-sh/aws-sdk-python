"""Generated from Smithy shape ``com.amazonaws.route53profiles#DisassociateResourceFromProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53profiles.types.arn
    import capo_route53profiles.types.resource_id


class DisassociateResourceFromProfileRequest(TypedDict, closed=True):
    profile_id: "capo_route53profiles.types.resource_id.ResourceId"
    """<p> The ID of the Profile. </p>"""
    resource_arn: "capo_route53profiles.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateResourceFromProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateResourceFromProfileRequest:
    out: DisassociateResourceFromProfileRequest = {}  # type: ignore[typeddict-item]
    return out
