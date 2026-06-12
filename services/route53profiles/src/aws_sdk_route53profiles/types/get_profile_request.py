"""Generated from Smithy shape ``com.amazonaws.route53profiles#GetProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.resource_id


class GetProfileRequest(TypedDict):
    profile_id: "aws_sdk_route53profiles.types.resource_id.ResourceId"
    """<p> ID of the Profile. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProfileRequest:
    out: GetProfileRequest = {}  # type: ignore[typeddict-item]
    return out
