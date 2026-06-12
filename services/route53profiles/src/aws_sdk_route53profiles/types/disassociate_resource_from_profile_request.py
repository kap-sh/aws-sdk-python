"""Generated from Smithy shape ``com.amazonaws.route53profiles#DisassociateResourceFromProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.arn
    import aws_sdk_route53profiles.types.resource_id


class DisassociateResourceFromProfileRequest(TypedDict):
    profile_id: "aws_sdk_route53profiles.types.resource_id.ResourceId"
    """<p> The ID of the Profile. </p>"""
    resource_arn: "aws_sdk_route53profiles.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateResourceFromProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateResourceFromProfileRequest:
    out: DisassociateResourceFromProfileRequest = {}  # type: ignore[typeddict-item]
    return out
