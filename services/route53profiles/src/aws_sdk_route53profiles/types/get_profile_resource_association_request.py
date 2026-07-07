"""Generated from Smithy shape ``com.amazonaws.route53profiles#GetProfileResourceAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.resource_id


class GetProfileResourceAssociationRequest(TypedDict, closed=True):
    profile_resource_association_id: (
        "aws_sdk_route53profiles.types.resource_id.ResourceId"
    )
    """<p> The ID of the profile resource association that you want to get information about. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileResourceAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProfileResourceAssociationRequest:
    out: GetProfileResourceAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
