"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetAccessTokenInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class GetAccessTokenInput(TypedDict, closed=True):
    access_token_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessTokenInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccessTokenInput:
    out: GetAccessTokenInput = {}  # type: ignore[typeddict-item]
    return out
