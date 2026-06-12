"""Generated from Smithy shape ``com.amazonaws.route53profiles#GetProfileAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.resource_id


class GetProfileAssociationRequest(TypedDict):
    profile_association_id: "aws_sdk_route53profiles.types.resource_id.ResourceId"
    """<p> The identifier of the association you want to get information about. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProfileAssociationRequest:
    out: GetProfileAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
